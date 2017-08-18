#! python3
#! /usr/bin/env python3

# Chapter 15 Practice Prettified Stopwatch
# Simple Stop Watch Program

# NOTE: Writing output to data text file rather than use pyperclip module.
#       Then file can be attached to email or copied as needed. And a
#       separate module outside the standard library is not required.

import time
import datetime

dataFile = open('stopWatchData.txt', 'a')

dt = datetime.datetime.now()
timeStamp = dt.strftime('\n%m/%d/%Y %H:%M\n')
dataFile.write(timeStamp)

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
        print('Lap #%s: %s (%s)' % (str(lapNum).ljust(2), str(totalTime).rjust(4), str(lapTime).rjust(5)), end='')
        dataFile.write('Lap #%s: %s (%s)\n' % (str(lapNum).ljust(2), str(totalTime).rjust(4), str(lapTime).rjust(5)))
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')

dataFile.close()
