class Player():
    def __init__(self, name):
        self.name=name
        self.chip_balance = 500
        self.hand = []
    
    def reset_balance(self):
        self.chip_balance = 500

    def card_add(self,new_card):
        self.hand append(new_card)

    