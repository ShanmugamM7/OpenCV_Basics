import cv2 as cv
import numpy as np

img =  cv.imread('Lord_siva.jpg')
cv.imshow('original',img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#bluring image
# blur = cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

#canny edge
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny', canny)

#Threshold
ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours are present!')

cv.drawContours(blank, contours, -1,(0,255,230), 2)
cv.imshow('contours',blank)
cv.waitKey(0)