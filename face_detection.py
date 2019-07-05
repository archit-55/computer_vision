#!/usr/bin/python3

import  cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('face.xml')



cap=cv2.VideoCapture(0)
while cap.isOpened() :
    status,frame=cap.read()  # continue image taker
    faces = face_cascade.detectMultiScale(frame,1.15,5)  
    for  (x,y,w,h) in faces:
        # Only face
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,225),2)
    cv2.imshow("window 1",frame)
    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
