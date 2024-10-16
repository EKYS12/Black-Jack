class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        # String representation of object
        card_str = f'{self.value} of {self.suit}'
        return card_str
