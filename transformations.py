import cv2 as cv
import numpy as np
img = cv.imread('Lord_siva.jpg')

#transformation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
"""
    -x ---> left
    -y ---> up
    x ---> right
    y ---> down
                """
#rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint =  (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

translated = translate(img, -100, -100)
cv.imshow('translated',translated)

rotated = rotate(img,90)
cv.imshow('rotated',rotated)


#resized
# resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

#flipped
flipped = cv.flip(img,-1)
"""
#second parameter is flipcode
0  ---> vertical flip
1 ----> horizontal flip
-1 ---> both vertical and horizontal flip
"""
cv.imshow('flipped',flipped)

#cropping
cropped = img[100:200, 200:300]
cv.imshow('cropped',cropped)

cv.waitKey(0)