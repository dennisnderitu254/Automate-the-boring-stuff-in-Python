#!python3
# Chap7PracStrip
# Remove whitespace from beginning and end of string using regex

import re

def remspace(string):
    global stringrem
    bspaceRegex = re.compile(r'\s*$')
    fspaceRegex = re.compile(r'^\s*')
    stringrem = bspaceRegex.sub('', string)
    stringrem = fspaceRegex.sub('', stringrem)
    return stringrem

remspace('    here is the string    ')
print(stringrem)
