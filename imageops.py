#!/usr/bin/python3
import  sys
import   cv2

###   version  
print(cv2.__version__)
#  image  name as  first  argu
data=sys.argv[1]

###   image read  
img=cv2.imread(data,1)     #  loading  image  in  a  colored  format  --original image 
img1=cv2.imread(data,0)     #  loading  image  in  gray scale  --BW 
print(img)

#  shape 
print(img.shape)

#   height , width ,  color channel 
#   to show  the image 
cv2.imshow('windowname',img)
cv2.imshow('windowname1',img-50)
cv2.imshow('windowname2',img[0:200,0:600]+100)
cv2.imshow('windowname3',img/2)
cv2.imshow('windowname4',img1)

#   saving  image
cv2.imwrite('newdog.jpg',img1)  

cv2.waitKey(0)   #   holding  window  for infinite  time
