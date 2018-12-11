import cv2
import numpy as np

bannanaCascade = cv2.CascadeClassifier('./test2/cascade.xml');
stop=False;
cap = cv2.VideoCapture(0);
while True:
    ret,frame = cap.read();
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    banannas = bannanaCascade.detectMultiScale(gray,300,300);

    for (x,y,w,h) in banannas:
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,'Bananna',(x-w,y-h),font,0.5,(0,255,255),2,cv2.LINE_AA)
        # cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,255),thickness)
    cv2.rectangle(frame,(10,10),(70,70), (255,255,0),3)
    cv2.imshow('img',frame);
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break
    if not stop :
    	width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
    	height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
    	print("Height: " + str(height) + "\nWeight: "+ str(width))

cap.release()
cv2.destroyAllWindows();
