values = {'A':11,'K':10,'Q':10,'J':10,'10':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

class Card ():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    __suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
    __ranks = ('A','K','Q','J','10','9','8','7','6','5','4','3','2')
    def __init__(self):
        self.deck=[]
        for suit in self.__suits:
            for rank in self.__ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        return f"Deck has {len(self.deck)} cards."



deck = Deck()