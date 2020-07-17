import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hls = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('hls',hls)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()