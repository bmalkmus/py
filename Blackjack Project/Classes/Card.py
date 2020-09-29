suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
rank = ('Ace','King','Queen','Jack','Ten','Nine','Eight','Seven','Six','Five','Four','Three','Two')
values = {'Ace':11,'King':10,'Queen':10,'Jack':10,'Ten':10,'Nine':9,'Eight':8,'Seven':7,'Six':6,'Five':5,'Four':4,'Three':3,'Two':2}

class Card ():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        print(f"{self.rank} of {self.suit}")
