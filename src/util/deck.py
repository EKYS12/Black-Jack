import numpy as np
from util.card import Card

class Deck:
    def __init__(self):
        # Values of Cards
        self.values = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

        # Suit of Cards
        self.suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

        self.stack = []

        for suit in self.suits:
            for value in self.values:
                self.stack.append(Card(value, suit))

    def __str__(self):
        '''
        String Print out of deck
        '''

        deck_str = ''

        for card in self.stack:
            deck_str = deck_str + f'\n{card}'

        return deck_str

    def shuffle(self, seed=0000):
        '''
        Method that scrambles deck

        seed: Default=1000. Seed number for reproducable shuffles.
        '''

        np.random.seed(seed)

        print(f'\n\nRandomSeed: {seed}')

        np.random.shuffle(self.stack)

    def draw(self):
        if self.stack:
            return self.stack.pop(0)
        else:
            raise ValueError('Deck is empty')

