import cv2
from resizeRescale import rescale_frame

#show original image
org = cv2.imread('Lesson 1 - Basics/coding_meme.jpeg')
circ = cv2.imread('Lesson 1 - Basics/coding_meme copy.jpeg')
cv2.imshow('Meme', org)

cv2.waitKey(1500)

### Part 1 - Rescale

#rescaled image
rescale = rescale_frame(org, 0.5)
cv2.imshow('MemeRescale', rescale)

cv2.waitKey(1500)


### Part 2 - Draw a circle

#Find center dimensions of image
center_width = int((org.shape[1])/2)
center_height = int((org.shape[0])/2)

#circle
circ = cv2.circle(circ,(center_width,center_height),90,(242,194,203),thickness=10)
cv2.imshow('MemeCircle', circ)

cv2.waitKey(1500)

### Part 3 - Image filter showcase

#greyscale  
greyscale=cv2.cvtColor(org,cv2.COLOR_BGR2GRAY)
cv2.imshow('MemeGrey', greyscale)

cv2.waitKey(1500)

# blured  
blur = cv2.GaussianBlur(org,(9,9),cv2.BORDER_DEFAULT)
cv2.imshow('MemeBlur', blur)

cv2.waitKey(1500)

#greyscale blured canny rescaled circle 
canny = cv2.Canny(org,125,200)
cv2.imshow('MemeCanny', canny)

cv2.waitKey(1500)

### Part 4 - Rotation

rotPoint=(center_width,center_height)
rotMat = cv2.getRotationMatrix2D(rotPoint,45,scale=1.0)
dimensions =(2*center_width,2*center_height)
rotated = cv2.warpAffine(org,rotMat,dimensions)
cv2.imshow('MemeRotate', rotated)


cv2.waitKey(1500)
