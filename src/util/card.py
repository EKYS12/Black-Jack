class Card:
    def __init__(self, value, suit, face=False, ace=False):
        self.value = value
        self.suit = suit

        if self.value in ['J', 'Q', 'K']:
            self.face = True
            self.point = 10 
        elif self.value == 'A':
            self.ace = True
            self.point = 11  
        else:
            self.point = int(self.value)

    def __str__(self):
        # String representation of object
        card_str = f'{self.value} of {self.suit}'
        return card_str

