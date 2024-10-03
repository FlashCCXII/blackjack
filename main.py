#from replit import clear

import random

from art import logo

def blackjack():
  print(logo)
  playgame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if playgame == "y":
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    usercards = []
    computercards = []
    for card in range(2):
      usercards.append(random.choice(cards))
      computercards.append(random.choice(cards))
    print(f"Your cards: {usercards}")
    print(f"Computers first card: {computercards[0]}")
    def check_blackjack():
      total = 0
      for card in usercards:
        total += card
      if total == 21:
        print(f"Your final hand: {usercards}\n")
        print(f"Computer's final hand: {computercards}")
        print("You got blackjack, you win!")
#       clear()
        blackjack()
      dealertotal = 0
      for card in computercards:
        dealertotal += card
      if dealertotal == 21:
        print(f"\nYour final hand: {usercards}")
        print(f"Computer's final hand: {computercards}")
        print("The Dealer got blackjack, you lose.")
      #       clear()
        blackjack()
    def addtotal():
      global total 
      total = 0
      for card in usercards:
        total += card
      if total > 21:
        print(f"\nYour final hand: {usercards}")
        print(f"Computer's final hand: {computercards}")
        print("You bust! Dealer wins.")
        blackjack()
      global dealertotal
      dealertotal = 0
      for card in computercards:
        dealertotal += card
      if dealertotal > 21:
        print(f"\nYour final hand: {usercards}")
        print(f"Computer's final hand: {computercards}")
        print("Dealer busts. You win!")
      if total == 21:
        print(f"\nYour final hand: {usercards}")
        print(f"Computer's final hand: {computercards}")
        print("You got 21, you win!")
#       clear()
        blackjack()
      if dealertotal == 21:
        print(f"\nYour final hand: {usercards}")
        print(f"Computer's final hand: {computercards}")
        print("The Dealer got 21, you lose.")
#       clear()
        blackjack()
    def dealerchoice():
      dealertotal = 0
      for card in computercards:
        dealertotal += card
      if dealertotal <= 16:
        computercards.append(random.choice(cards))
        dealerchoice()
      else:
        return
    def hitorhold():
      check_blackjack()
      decision = input("Type 'hit' to get another card, type 'stand' to pass: ")
      if decision == "hit":
        usercards.append(random.choice(cards))
        dealerchoice()
        print(f"Your cards: {usercards}")
        addtotal()
        hitorhold()
      else:
        print(f"Your final hand: {usercards}")
        dealerchoice()
        addtotal()
    hitorhold()
    print(f"Computer's final hand: {computercards}")

    
    if total == dealertotal:
      print("It's a tie!")
#     clear()
      blackjack()
    if total > dealertotal:
      print("You Win!")
#      clear()
      blackjack()
    else:
      print("You lose.")
#      clear()
      blackjack()
  else:
    print("Goodbye!")
    return

blackjack()
