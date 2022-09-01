import cv2 as cv
import numpy as np
from PIL import ImageGrab
import time

time.sleep(2)

def drawBox(img,bbox): 
    x,y,w,h = (bbox[0]),(bbox[1]),(bbox[2]),(bbox[3]) # convert bbox 
    cv.rectangle(img,(x,y),((x+w),(y+h)),(255,30,150),2) # draw a rectangle on the object
    
img = ImageGrab.grab(bbox=(0,0,1920,1080)) # print function
img = cv.cvtColor(np.array(img), cv.COLOR_BGR2RGB) # convert color to rgb

roi = cv.selectROI("opencv", img, False) # init the selector
tracker = cv.TrackerKCF_create() # create the tracker model
tracker.init(img, roi) # init the tracker

cv.namedWindow("opencv", cv.WINDOW_NORMAL) # resizable windows
def main():
    img = ImageGrab.grab(bbox=(0,0,1920,1080)) #  
    frame = np.array(img)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    sucess, bbox = tracker.update(frame)
    print("isOnScreen: {}".format(sucess),"|" "coordinate: {}".format(bbox))
    
    if sucess:
        drawBox(frame,bbox)
    else:
        cv.putText(frame,"lost track",(500,500),cv.FONT_HERSHEY_COMPLEX,2,(0,0,255),1,1)
    
    cv.imshow("opencv", frame)    
    
if __name__ == '__main__':
    while 1:
        main()
        if cv.waitKey(1) == 27:
            break 
