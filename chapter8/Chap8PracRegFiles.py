#! \usr\bin\env python3

# Chapter 8 Practice Regex Text Files

# Opens all .txt files in a folder and
# then searches for any line that matches
# a user-supplied regular expression.

import os
import re

dirfiles = os.listdir('C:\\gam')

print('What text do you want to search for?')
userReg = str(input())
stringRegex = re.compile(userReg)
fileRegex = re.compile(r'\w+\.txt')

for i in range(len(dirfiles)):
    if fileRegex.search(dirfiles[i]):
        openFile = open('C:\\gam\\' + dirfiles[i])
        readFile = openFile.readlines()
        for line in range(len(readFile)):
            r = 0
            if stringRegex.search(readFile[r]):
                print(readFile[r])
                r = r + 1


