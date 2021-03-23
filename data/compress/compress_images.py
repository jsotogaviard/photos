#!/usr/bin/env python
# encoding: utf-8
"""
compress.py
"""

from PIL import Image, ImageFile
import PIL
import os
import glob
from sys import argv
ImageFile.LOAD_TRUNCATED_IMAGES = True

def compress_images(directory=False, quality=30):
    # 1. If there is a directory then go to it, else perform the next operations inside of the 
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if (file.endswith('jpg') and not file.__contains__('quality'))]

    # 4. Loop over every image:
    print(os.getcwd())
    for image in images:

        # 5. Open every image:
        img = Image.open(image)
        print('{:4.0f}'.format(os.stat(image).st_size/1000) + "kb :" + image)
        # 5. Compress every image and save it with a new name:
        start = image.split('.')[0]
        end = image.split('.')[1]
        img.save(start + "_quality_" + str(quality) + "."+end, optimize=True, quality=quality)

    # 6 Print result
    print(os.getcwd())
    for image in os.listdir():
        print('{:4.0f}'.format(os.stat(image).st_size/1000) + "kb :" + image)

if __name__ == '__main__':
    directory = argv[1]
    quality = int(argv[2])
    compress_images(directory, quality)