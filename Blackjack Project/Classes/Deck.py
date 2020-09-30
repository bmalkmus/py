
import Card

suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
ranks = ('A','K','Q','J','10','9','8','7','6','5','4','3','2')

class Deck():
    def __init__(self,suits,ranks):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card.Card(suit,rank))

    def __str__(self):
        return f"Deck has {len(self.deck)} cards."

deck = Deck(suits,ranks)

print(deck)