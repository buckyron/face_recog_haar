import cv2
import numpy as np 
from time import sleep

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,minNeighbors=5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        for i in range(0,99):
            img_item = 'image{}.png'
            cv2.imwrite(img_item.format(i), roi_gray)
            

        color = (255,0,0)
        stroke = 4
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame,(x,y), (end_cord_x,end_cord_y), color, stroke)





    cv2.imshow('frame',frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()