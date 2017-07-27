#! /usr/bin/env python3

# Practice Chap. 7
# Password Strength Tester

import re

def passStrengthTest(passWord):
    lowerRegex = re.compile(r'[a-z]')
    upperRegex = re.compile(r'[A-Z]')
    numRegex = re.compile(r'[0-9]')
    molower = lowerRegex.search(passWord)
    moupper = upperRegex.search(passWord)
    monum = numRegex.search(passWord)
    if len(passWord) < 8:
        print('Your password is less than 8 characters which is too short.')
    elif not molower:
        print('You need at least one lower case letter.')
    elif not moupper:
        print('You need at least one upper case letter.')
    elif not monum:
        print('You need at least one number.')
    else:
        print('Your password is strong!')


print('What is your password?')
passW = input()
passStrengthTest(passW)

