#! python3

# Chapter 18 Practice Looking Busy
# Moves the mouse cursor ever 15 seconds to trick the computer into
# thinking you are still busy working.

import time
import pyautogui


print('Press CTRL-C to End')

try:
    while True:
        pyautogui.moveRel(-100, 0)
        pyautogui.moveRel(100, 0)
        time.sleep(15)
except KeyboardInterrupt:
    print('\nEnded')
