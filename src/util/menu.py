import sys
import game

print('Welcome to Black Jack')

print('Would you like to play?')

print('\n1. Yes, start a game')
print('\n2. No, exit')

not_valid_input = True

while not_valid_input:
    user_input = int(input('Choice: '))

    if user_input in [1,2]:
        not_valid_input = False

    else:
        print('Invalid input, try again')

if user_input == 1:
    game


if user_input == 2:
    sys.exit()
