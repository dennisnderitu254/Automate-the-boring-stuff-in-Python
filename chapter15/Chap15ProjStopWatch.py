#! python3
#! /usr/bin/env python3

# Chapter 15 Project Super Stopwatch
# Simple Stop Watch Program

import time

print('Press ENTER to begin. Afterwards, press ENTER to click the stopwatch.')
print('Press CTRL-C to quit.')
input()
print('Started...')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime  = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')
