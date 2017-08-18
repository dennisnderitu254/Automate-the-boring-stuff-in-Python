#!/usr/bin/env python3

#Chapter 11 Project
# lucky.py - Opens several Google search results

import requests
import sys
import webbrowser
import bs4

print('Googling...') #Display message while retrieving the Google page

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('htpp://google.com' + linkElems[i].get('href'))
