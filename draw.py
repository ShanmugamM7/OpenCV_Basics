import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("Blank_Image",blank)

#painting the image with a certain color
#blank[:] = 0,255,0    #represents all the pixels with green color\
blank[0:300, 300:500] = 0,255,0
# cv.imshow("Green",blank)

# drawing rectangle in the image
# cv.rectangle(blank,(0,0),(255,255), (0,0,255), thickness=1)
cv.rectangle(blank,(100,10),(255,255), (0,0,255), thickness=cv.FILLED) #-1 is equivalent to cv.FILLED
# cv.imshow('rectangle', blank)

#drawing circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),30,(255,0,0),thickness=2)
# cv.imshow('Cirlce',blank)

#drawing a line
cv.line(blank,(120,120),(230,240),(255,255,0),thickness=4)
# cv.imshow('line',blank)

# write text
cv.putText(blank,'Test_demo', (300,300),cv.FONT_HERSHEY_SIMPLEX,1,(255,123,234),3)
cv.imshow('text',blank)
cv.waitKey(0)