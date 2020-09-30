class Player():
    chip_balance = 500
    hand = []
    bet = 0
    def __init__(self, name):
        self.name=name

    def __str__(self):
        return f"Player: {self.name} Balance: {self.chip_balance}"
    
    def reset_balance(self):
        self.chip_balance = 500

    def card_add(self,new_card):
        self.hand.append(new_card)

    def set_bet(self):
        if self.bet == 0 or self.bet > self.chip_balance:
            while self.bet == 0 or self.bet > self.chip_balance:
                try:
                    self.bet = int(input(f"How much would you like to bet out of your balance of {self.chip_balance}?"))
                except:
                    print("Sorry that is not a valid number")

                if(self.bet > self.chip_balance):
                        print("Sorry you do not have that much to bet :(")
        else:
            answer_choices = ["YES", "NO"]
            answer = ""
            while answer not in answer_choices:
                answer = input(f"Would you like to use your previous bet of {self.bet}? (yes or no)").upper()

                if answer == "NO":
                    previous = self.bet
                    while self.bet == previous or self.bet > self.chip_balance:
                        try:
                            self.bet = int(input(f"How much would you like to bet out of your balance of {self.chip_balance}?"))
                            if self.bet == previous:
                                confirm = ""
                                while confirm not in answer_choices:
                                    confirm = input("That was your previous bet amount, are you sure to continue? (yes or no)").upper()
                                if confirm == "YES":
                                    break
                                
                        except:
                            print("Sorry that is not a valid number")

                        if(self.bet > self.chip_balance):
                                print("Sorry you do not have that much to bet :(")



