from classes.Player import Player
from classes.Deck import Deck
import random

deck = Deck()
computer_hand = []
player = Player(input("Please enter your name: "))

def display_cards():
    computer_display = []
    player_display = []

    for card in computer_hand:
        computer_display.append(f"|{card.rank}|")

    for card in player.hand:
        player_display.append(f"|{card.rank}|")
    
    computer_display[0] = "|?|"
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Computer's hand:")
    print(computer_display)
    print("\n\n\n\n")
    print("Your Hand:")
    print(player_display)

def computer_hit():
    computer_hand.append(deck.remove_top())

def player_hit():
    player.hand.append(deck.remove_top())

def initial_deal():
    player.hand.append(deck.remove_top())
    computer_hand.append(deck.remove_top())
    player.hand.append(deck.remove_top())
    computer_hand.append(deck.remove_top())

def sum_hand(hand):
    temp = []
    for card in hand:
        temp.append(card.value)
    while 11 in temp:
        if sum(temp) > 21:
            temp.sort()
            temp[-1]=1 
    return sum(temp)

def round():
    # player.set_bet()
    computer_display = []
    initial_deal()
    player_hit()
    display_cards()
    sum_hand(player.hand)



def game_play():
    while player.wants_to_play==True and player.chip_balance > 0:
        round()
        print ("here I am")
        # ------------------Make sure to remove this break below----------------------
        break
    if player.chip_balance == 0:
        print(f"I'm sorry {player.name}, It appears you have no more chips to bet")

game_play()