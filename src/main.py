import cv2 as cv
import numpy as np
from PIL import ImageGrab
import time

input("press enter to start!")
time.sleep(1)

def drawBox(img, bbox):
    x, y, w, h = (bbox[0]), (bbox[1]), (bbox[2]), (bbox[3]) 
    cv.rectangle(img, (x, y), ((x + w), (y + h)), (255, 30, 150), 2)


img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
img = cv.cvtColor(np.array(img), cv.COLOR_BGR2RGB)

roi = cv.selectROI("opencv", img, False) ## select image to track
tracker = cv.TrackerCSRT_create() ## define the tracking algorithm
tracker.init(img, roi) 

cv.namedWindow("opencv", cv.WINDOW_NORMAL) ## make the window resizable


def main():
    frame =         ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    frame =         cv.cvtColor(np.array(frame), cv.COLOR_BGR2RGB)
    sucess, bbox =  tracker.update(frame)
    ## remove the comment to see debug
    #print("isOnScreen: {}".format(sucess),"|" "coordinate: {}".format(bbox))

    if sucess:
        drawBox(frame, bbox)
    else:
        cv.putText(frame, "lost track", (500, 500),
                   cv.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 1, 1)

    cv.imshow("opencv", frame)


if __name__ == '__main__':
    while True:
        main()
        if cv.waitKey(1) == 27: ## opencv required
            break
