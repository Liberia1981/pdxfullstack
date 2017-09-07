

class Card:
    def __init__(self, suit):
        self.suit = suit

    def print_value(self):
        print(self.suit)

car1 = Card('Hearts')
print(car1)
car1.print_value()
