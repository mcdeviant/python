#!/usr/bin/python3
#Guess the number game
import random

print('Hi, what is your name?')
NAME = input()

print('Hello there ' + NAME + ', I am thinking of a number between 1 and 20.')
NUMBER = random.randint(1, 20)

for GUESSES_TAKEN in range(1, 7):
    print('Take a guess.')
    GUESS = int(input())

    if GUESS < NUMBER:
        print('Too low! Shoot higher!')
    elif GUESS > NUMBER:
        print('Too high! Try again!')
    else:
        break #breaks loop on accurate guess

if GUESS == NUMBER:
    print('Congratulations ' + NAME + '! You took ' + str(GUESSES_TAKEN) + ' guesses to reach my number!')
else:
    print('Sorry ' + NAME + ' , you ran out of guesses and the correct answer was ' + str(NUMBER))
