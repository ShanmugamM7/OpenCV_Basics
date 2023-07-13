import cv2 as cv

#reading image
# img = cv.imread("Lord_siva.jpg")

# cv.imshow('Siva', img)

#reading existing video
capture = cv.VideoCapture(0)

while True: 
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()

cv.destroyAllWindows()
#cv.waitKey(0)