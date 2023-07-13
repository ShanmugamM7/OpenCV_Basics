import cv2 as cv

# img = cv.imread('Lord_siva.jpg')
# cv.imshow('original_image', img)

#function for rescaling the original image
def rescaleFrame(frame, scale=1):
    #works for images, videos(recoreded or live)
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)

    #initalizing the resized dimensions
    dimensions = (height, width)
    print(dimensions)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#funtion for resoultion change
def changeRes(height,width):
    #works only for live videos
    capture.set(4,height)
    capture.set(4,width)
#Video Capture
capture = cv.VideoCapture("Teju.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Original_frame', frame)
    cv.imshow('Resized_frame', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()