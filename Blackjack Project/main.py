from classes.Player import Player
from classes.Deck import Deck

deck = Deck()
player = Player(input("Please enter your name: "))

def round():
    player.set_bet()



def game_play():
    while player.wants_to_play==True and player.chip_balance > 0:
        round()
        print ("here I am")
        # ------------------Make sure to remove this break below----------------------
        break
    if player.chip_balance == 0:
        print(f"I'm sorry {player.name}, It appears you have no more chips to bet")
        
game_play()