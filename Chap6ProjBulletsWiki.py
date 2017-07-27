#! /usr/bin/env python3

# Bullets to Wiki Markup Chap. 6
# Copies text from clipboard, adds a star to each line, pastes to clipboard.

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
