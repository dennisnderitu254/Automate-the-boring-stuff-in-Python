#! ptyhon3

# Chapter 8 Practice Project
# Extend the Multiclipboard project to include a delete option


# Loads and saves clipboard text based on a key word from the command line
# Usage: py.exe mcb.pyw save <keyword> - Saves to clipboard
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard
#        py.exe mcb.pyw delete - Deletes all keywords
#        py.exe mcb.pyw delete <keyword> - Deletes a specific keyword

import sys
import pyperclip
import shelve

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for k in list(mcbShelf.keys()):
                      del mcbShelf[k]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
