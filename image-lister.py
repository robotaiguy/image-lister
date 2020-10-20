#
# image-lister.py
# Lists in a text file, sorted by name, the images (jpg and png) found in images directory 
# Developed by Scott Uneberg, https://github.com/robotwhispering 
# Under MIT License
# Updated 10/19/2020
#

import glob
from pathlib import Path

# set path to images directory
images_path = './images'

# create and/or truncate image-list.txt
image_list = open("image-list.txt", "w")

# initialize image_cnt counter and images_array
image_cnt = 0
images_array = []

# append images_array with each image found in directory
for imagename in Path(images_path).rglob("*.jpg"):
    images_array.append(str(imagename.resolve()))
    image_cnt += 1

for imagename in Path(images_path).rglob("*.png"):
    images_array.append(str(imagename.resolve()))
    image_cnt += 1

# sort images_array by name
images_array.sort()

# populate image-list.txt with path of each image found in images directory
for image in images_array:
    image_list.write(image + "\n")

# print total number of listed images to console
print("Number of images: " + str(image_cnt))

