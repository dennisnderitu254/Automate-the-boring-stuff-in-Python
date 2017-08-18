#!/usr/bin/env python3

# Chapter 10 Practice Debugging Coin Toss

import random

guess = ''
while guess not in (int(1), int(0)): #Changed heads and tails to 1 and 0 and made integers
    print('Guess the coin toss! Enter 1 for heads or 0 for tails:') #Added 1 and 0
    guess = int(input()) #Turned string into integer

toss  = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = int(input()) #guess misspelled with three 's' instead of two and made guess integer
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
