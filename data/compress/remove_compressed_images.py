#!/usr/bin/env python
# encoding: utf-8
"""
remove_compressed.py
"""


import os

from sys import argv

def remove_compressed_images(directory=False):
    # current working directory:
    if directory:
        os.chdir(directory)

    files = os.listdir()
   
    compressed_images = [file for file in files if file.__contains__('quality')]

    print(os.getcwd())
    for compressed_image in compressed_images:
        print("deleted: "+ compressed_image)
        os.remove(compressed_image)
    
    currentDir = os.getcwd()
    subfolders = [f for f in os.scandir(currentDir) if f.is_dir()]
    for subfolder in subfolders:
        remove_compressed_images(subfolder)

if __name__ == '__main__':
    directory = argv[1]
    remove_compressed_images(directory)