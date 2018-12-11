import cv2
import numpy as np

gumCover =cv2.CascadeClassifier('./data/cascade.xml');

img = cv2.imread('testImage2.jpg');
gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#increasing the number of neighbors does work
gumCovers = gumCover.detectMultiScale(gray,3.5,30);
count=0;
for (x,y,w,h) in gumCovers:
    count= count+1;
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
print(count);

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
