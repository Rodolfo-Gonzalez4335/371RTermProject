import cv2
import numpy as np

gumCover =cv2.CascadeClassifier('./data/cascade.xml');

img = cv2.imread('testImage.jpg');
gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#increasing the number of neighbors does work
gumCovers = gumCover.detectMultiScale(gray,1.3,2);

for (x,y,w,h) in gumCovers:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
