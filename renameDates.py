#!python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

"""
Here is what the program does

1.It searches all the filenames in the current working directory for
  American-style dates.
2.When one is found, it renames the file with the month and day swapped
  to make it European-style.

This means the code will need to do the following:

1.Create a regex that can identify the text pattern of American-style dates.

2.Call os.listdir() to find all the files in the working directory.

3.Loop over each filename, using the regex to check whether it has a date.

4.If it has a date, rename the file with shutil.move()

"""

import shutil, os, re

# Create a regex that matches files with the American date format.

datePattern = re.compile(r"""^(.*?)    # all text before the date
	((0|1)?\d)-                        # one or two digits for the month
	((0|1|2|3)?\d)-                    # one or two digits of the day
	((19|20)\d\d)                      # four digits for the year
	(.*?)$                             # all text after the date
	""", re.VERBOSE)


# TODO: Loop over the files in the working directory.

for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	# Skip files without a date.
	if mo == None:
		continue

	# Get the different parts of the filename.
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart =  mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	#Form the European-style filename.

	euroFilename = beforePart+dayPart+ '-' + monthPart + '-' + yearPart + afterPart

	# Get the full, abso;ute file paths.

	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	# Rename the files.
	print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
	#shutil.move(amerFilename, euroFilename) # uncomment after testing








