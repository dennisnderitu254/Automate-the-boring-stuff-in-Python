#!python

# Chapter 9 Practice Selective Copy
# Walks through a directory tree searching for pdf files and copies them to a new location

import os
import shutil

def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.endswith('.pdf'):
                continue
            #shutil.copy(filename, 'c:\\pdffolder') #Commented out to protect against accidental copying
            print('Copying ' + filename + '...') #Print only to verify working correctly

selectiveCopy(r'C:\Users\username\pdffolder')
print('Done')
