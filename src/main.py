from util.deck import Deck

print('This is main.')

print('\nThis is a fresh deck of card.')
deck = Deck()
print(deck)

seed = 0000
deck.shuffle(seed=seed)

print(f'\nThis is the deck shuffled with seed {seed}')
print(deck)
