#!/usr/bin/python3

"""
Author:			John-Philipp Vogt
Date:			2022-08-05
Synopsis:		A simple guess-the-number game.
Filename:		guessTheNumber.py
"""

import random

secretNumber = random.randint(1, 20)

print('I\'m thinking of a number between 1 and 20')

# Ask user to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # Correct guess-condition
        
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

