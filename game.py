"""
Prompts the user for a level,
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.

"""

from operator import gt
import random
import sys

invalid_guess = True
invalid_level = True

while invalid_level:
    level = input("Level: ")
    if level.isdigit():
        invalid_level = False
answer = random.randint(1,int(level))

while invalid_guess:
    guess = input("Guess: ")
    if guess.isdigit():        
        if int(guess) == int(answer):
            sys.exit('Just Right!')
        if int(guess) > int(answer):
            print('Too large!')
        if int(guess) < int(answer):
            print('Too small!')
        #invalid_guess = False
