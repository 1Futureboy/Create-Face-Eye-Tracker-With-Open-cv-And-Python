import numpy as np
import cv2


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")



cap=cv2.VideoCapture(2)

while cap.isOpened():
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.2,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        eye=eye_cascade.detectMultiScale(roi_gray,1.2,5)
        for(ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

        cv2.imshow("suscribe",frame)
        if cv2.waitKey(1) & 0xff==ord("r"):
            break


cap.release()
cv2.destroyAllWindows()





    
    
