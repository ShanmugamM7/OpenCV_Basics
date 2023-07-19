"""
=============================================================
Created by
        Shanmugam Machaa[19/07/2023-13:50]
=============================================================
>> Getting started with images: to read, show and write
"""

#importing required modules
import cv2 as cv
import sys

# reading image
"""
>> first parameter is path of the image
>> second parameter can be:- IMREAD_COLOR >> Reads the image in BGR 8-bit format, it is default parameter.
                             IMREAD_UNCHANGED >> Reads the image as it is, including alpha channel if present.
                             IMREAD_GRAYSCALE >> Reads image in gray color.
"""
img = cv.imread("img1.jpg")

# Checks if given given is loaded or not
if img is None:
    sys.exit("The image provided is unable to load, please with that...")

#showing the image
"""
>> First parameter is window name to be displayed
>> Second parameter is the image which need to be shown
"""
cv.imshow('loaded image',img)

# Used to define how much time the image need to be displayed
# The parameter is just how longer it should wait for the user input(in milliseconds)
# if it is  0 >> Wait forever
k = cv.waitKey(0)

# if the pressed key is "s", the image get saved with specified name
# First parameter is name of the image to be saved.
# Second parameter is the image which need to be saved.
if k == ord("s"):
    cv.imwrite('first.jpg',img)