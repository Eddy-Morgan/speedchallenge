import cv2
import numpy as np


#This section configures text in frame

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (400,460)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

# This section read train speed txt file

with open("../data/train.txt","r") as fo:
    #This section trains with the video

    cap = cv2.VideoCapture("../data/train.mp4")
    while(cap.isOpened()):
        _, frame = cap.read()
        frameSpeed = fo.readline()
        cv2.putText(frame,frameSpeed, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)

        cv2.imshow("result",frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()