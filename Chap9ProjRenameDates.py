#!/usr/bin/env python3

#Chapter 9 Project Renaming File Dates from American to European

import os
import re
import shutil

datePattern = re.compile(r'''^(.*?) #All text before date
                         ((0|1)?\d)- #One or two month digits
                         ((0|1|2|3)?\d)- #One or two digits for month
                         ((19|20)\d\d) #Four digits for the year
                         (.*?)$ #all text after the date
                         ''', re.VERBOSE)


for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
