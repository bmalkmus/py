from classes.Player import Player
from classes.Deck import Deck
import random
import math

deck = Deck()
computer_hand = []
player = Player(input("Please enter your name: "))

def display_cards(turn):
    computer_display = []
    player_display = []

    for card in computer_hand:
        computer_display.append(f"|{card.rank}|")

    for card in player.hand:
        player_display.append(f"|{card.rank}|")
    
    if turn == 'PLAYER':
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
        else:
            break
    return sum(temp)

def player_turn():
    display_cards("PLAYER")
    if (sum_hand(player.hand) == 21):
        return "BLACKJACK"

    if (sum_hand(player.hand) > 21):
        return "BUST"

    player_choice=""
    options_list=["HIT", "STAY"]

    while player_choice not in options_list:
        player_choice=input(f"You have a value of {sum_hand(player.hand)}, would you like to Hit or Stay?").upper()
        if player_choice not in options_list:
            print("I'm sorry, that is not a valid choice option")
        if player_choice == "STAY":
            return "STAY"
        if player_choice == "HIT":
            player_hit()

def computer_turn():

    display_cards("Computer")

    if sum_hand(computer_hand) == 21:
        return "BLACKJACK"
    if sum_hand(computer_hand) > 21:
        return "BUST"
    if sum_hand(computer_hand) < 21 and sum_hand(computer_hand) >= 17:
        return "STAY"
    while sum_hand(computer_hand) < 17:
        computer_hit()
        
def round():
    player_result = ""
    computer_result = ""
    hand_result_list = ["BLACKJACK", "BUST", "STAY"]

    player.set_bet()

    deck.shuffle_deck()

    initial_deal()

    while player_result not in hand_result_list:
        player_result=player_turn()


    if player_result == "BLACKJACK":
        print(f"BLACK JACK! You have won {math.ceil(player.bet * 1.25)} chips")
        player.chip_balance = player.chip_balance + math.ceil(player.bet * 1.25)
        return player.chip_balance
    if player_result == "BUST":
        print(f"You have Busted, you lose {player.bet} chips")
        player.chip_balance = player.chip_balance - player.bet
        return player.chip_balance

    while computer_result not in hand_result_list:
        computer_result = computer_turn()


    if computer_result == "BLACKJACK":
        print(f"Computer had Blackjack. You lose {player.bet} chips")
        player.chip_balance = player.chip_balance - player.bet
        return player.chip_balance

    if computer_result == "BUST":
        print(f"Computer has busted. You win {player.bet} chips")
        player.chip_balance = player.chip_balance + player.bet
        return player.chip_balance

    computer_sum = sum_hand(computer_hand)
    player_sum = sum_hand(player.hand)

    if (computer_sum > player_sum):
        print(f"The computer hand: {computer_sum} \nPlayer hand: {player_sum} \n You lose {player.bet} chips")
        player.chip_balance = player.chip_balance - player.bet
    elif (computer_sum == player_sum):
        print(f"The computer hand: {computer_sum} \nPlayer hand: {player_sum} \n Its a draw. you win {math.ceil(player.bet * .5)} chips")
        player.chip_balance = player.chip_balance + math.ceil(player.bet * .5)
    else:
        print(f"The computer hand: {computer_sum} \nPlayer hand: {player_sum} \n You win {player.bet} chips")
        player.chip_balance = player.chip_balance + player.bet


def game_play():
    while player.wants_to_play==True and player.chip_balance > 0:
        another_round = ""
        round_options = ["YES", "NO"]
        round()
        deck.deck.extend(computer_hand)
        deck.deck.extend(player.hand)
        computer_hand.clear()
        player.hand.clear()
        while another_round not in round_options:
            another_round = input("Would you like to play another round? (YES OR NO) ").upper()
            if another_round not in round_options:
                print("I'm sorry that is not a valid response")
        
        if round_options == "NO":
            player.wants_to_play==False
    if player.wants_to_play == False:
        print("Thanks for playing, have a wonderful day!")
    if player.chip_balance == 0:
        print(f"I'm sorry {player.name}, It appears you have no more chips to bet")

game_play()