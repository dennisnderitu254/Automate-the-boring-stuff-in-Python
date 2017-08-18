#! /usr/bin/env python3

# Chapter 13 Practice Brute-Force PDF Password Breaker
# USAGE: Change the pdfFile varible below and run the script to try 44,000 English words
#           from the dictionary.txt file to decrypt the encrypted PDF.

import PyPDF2

pdfFile = open('bruteForce.pdf', 'rb') #Change this file name and location
pdfReader = PyPDF2.PdfFileReader(pdfFile)

dictionaryFile = open('dictionary.txt')
passwordList = dictionaryFile.readlines()

for word in range(len(passwordList)):
    passWord = passwordList[word].strip()
    passWorkedUpper = pdfReader.decrypt(passWord.upper())
    if passWorkedUpper == 1:
        print('The password is: ' + passWord.upper())
        break
    else:
        print(passWord.upper() + ' did NOT work...')
    passWorkedLower = pdfReader.decrypt(passWord.lower())
    if passWorkedLower == 1:
        print('The password is: ' + passWord.lower())
        break
    else:
        print(passWord.lower() + ' did NOT work...') 

dictionaryFile.close()
pdfFile.close()
                
