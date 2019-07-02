#!/usr/bin/python3

import  cv2

#  staring  camera
cap=cv2.VideoCapture(0)

#                   first  camera  
#  to check  camera is started or  not  
if  cap.isOpened() :
    print("camera is ready to take pictures")
else :
    print("check your web cam drivers  ")

#  now  we can take read  input  from camera
status,img=cap.read()              #  it  will take  first  picture 
status1,img1=cap.read()            #  it  will take  first  picture 

#  now showing  
cv2.imshow('liveimamge',img)
cv2.imshow('liveimamge1',img1)
cv2.waitKey(0)

#  to close camera
cap.release()
