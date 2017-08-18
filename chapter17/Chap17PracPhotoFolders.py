#! python3

# Chapter 17 Practice Indetifying Photo Folders on the Hard Drive

# Searches your hard drive for any (sub)folders that contain image files
# that are .png or .jpg that are at least 500 pixels in size or larger
# and prints their absolute path to the screen.

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('c:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if extension is not .png or .jpg
        if not filename.endswith('.png') or filename.endswith('.jpg'):
            numNonPhotoFiles += 1
            continue

        # Open image file using pillow. Skip file if error occurs.
        try: im = Image.open(os.path.join(foldername, filename))
        except: continue
        width, height = im.size

        # Check if width and height are larger than 500
        if width >= 500 and height >= 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

        # If more than half of files were photos,
        # print the absolute path of the folder.
        if numPhotoFiles > numNonPhotoFiles:
            print(foldername)
