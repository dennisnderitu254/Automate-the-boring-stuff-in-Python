#! /usr/bin/env python3

# Password Manager Chap. 6

PASSWORDS = {'email': 'ihwbrfh3rhbfwhbdifuhsud',
             'blog': '974y5h34kr73ihfi3',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password.')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('The password for ' + account + ' has been copied to the clipboard.')
else:
    print('There is no account named ' + account)

sys.exit()
