#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os


def backupToZip(folder):
	# Backup the entire contents of "Folder" into a ZIP file.

	folder = os.path.abspath(folder) # make sure folder is absolute

	#figure out the file naem this code should be based on
	# what file already exists.

	number = 1

	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1

		print('Creating %s...'% (zipFilename))
		backupZip = zipfile.ZipFile(zipFilename, 'w')

		# Walk the entire folder tree and compress the files in each folder.

		for foldername, subfolders, filenames in os.walk(folder):
			print('Adding files in %s...'%(foldername))
			# Add the current folder to the ZIP file.

			backupZIp.write(foldername)
			#Add all the files in this folder to the ZIP file.

			for filename in filenames:
				newBase/os.path.basename(folder) + '_'
				if filename.startswith(newBase) and filename.endswith('.zip'):
					continue # dont backuo the backup Zip files
				backupZip.write(os.path.join(foldername, filename))


			backupZip.close()
			print('Done.')



backupToZip('C:\\delicious')






