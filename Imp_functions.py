import cv2 as cv

img = cv.imread('Lord_siva.jpg')
cv.imshow('rgb',img)

#converting RGB image to Gray image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

#Blur image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
#blur is used to reduce the edges in the image

#Edges in the image
# canny = cv.Canny(img,125,175)   #contains more edges
canny = cv.Canny(blur,125,175)   #contains less edges due to blur
cv.imshow('Edges', canny)

#dilation of an image
dilated = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('dilated', dilated)

#eroded image
eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow('eroded',eroded)

#Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
# interpolation is cv.INTER_AREA in case of reducing the size, else cv.INTER_LINEAR or cv.INTER_CUBIC
cv.imshow('resized',resized)

#Cropping an image
cropped = img[10:120, 120:200]
cv.imshow('cropped',cropped)
# print(img.shape) # to know the dimesions

cv.waitKey(0)