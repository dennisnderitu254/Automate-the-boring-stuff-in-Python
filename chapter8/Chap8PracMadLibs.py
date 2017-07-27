#! \usr\bin\env python3

# Chapter 8 Practice Mad Libs

# Replaces all ADJECTIVE, NOUN, ADVERB, VERB keywords with user input in text.

import re


with open('madlibs.txt') as madLibFile:
    madLibContents = madLibFile.read()
madLibWords = list(madLibContents.split())

adjectiveRegex = re.compile(r'ADJECTIVE*')
nounRegex = re.compile(r'NOUN*')
adverbRegex = re.compile(r'ADVERB*')
verbRegex = re.compile(r'VERB*')

for i in range(len(madLibWords)):
    if adjectiveRegex.match(madLibWords[i]):
        print('Enter an adjective', end=': ')
        sub = input()
    elif nounRegex.match(madLibWords[i]):
        print('Enter a noun', end=': ')
        sub = input()
    elif adverbRegex.match(madLibWords[i]):
        print('Enter an adverb', end=': ')
        sub = input()
    elif verbRegex.match(madLibWords[i]):
        print('Enter a verb', end=': ')
        sub = input()
    else:
        continue
    madLibWords.remove(madLibWords[i])
    madLibWords.insert(i, sub)

joinWordsList = ' '
newString = joinWordsList.join(madLibWords)
with open('madlibsNew.txt', 'w') as newMadLibFile:
    newMadLibFile.write(newString)
print(newString)
