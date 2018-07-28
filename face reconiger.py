import numpy as np      #Importing numpy for metrices and mathematics 
import cv2              #Importing OpenCv Called Cv2 This Function Use For Image Analysis And Video Analysis


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   #This Is face_harrcascade this is face tracking cascade
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")                    #This Is eye_cascade this is eye tracking cascade



cap=cv2.VideoCapture(0) #In VideoCapture("You Want To Use A Camera Then Give A Camera Name If You Want To Track A Face And Eye In Video Then Give Video Location")    

while cap.isOpened():       #Here Start A While loop Becase We Want To Run A Program Continue   
    ret,frame=cap.read()    #Here frame Variable Store cap variable to read A Camera (video)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     #Converting A Video Into GRAY Mode
    face=face_cascade.detectMultiScale(gray,1.2,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # This Is Face Tracking Code It Run Accurate After Giving X Axis And Y Axis 

        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        eye=eye_cascade.detectMultiScale(roi_gray,1.2,5)
        for(ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2) #This Is X Axis And Y Axis Of Eye And Trace A Eye Accurate

        cv2.imshow("suscribe",frame)
        if cv2.waitKey(1) & 0xff==ord("r"): #This Is Use For Closing A Programm If I Hit A Key On Keyboard Then Program Is Stop 
            break #Here loop Is break means (Close)


cap.release()  #After Hit A Key On Keyboard This Code Is Running And Stop The Tracking
cv2.destroyAllWindows()  # After Stoping The Video This Code Is Running And Close The Programm





    
    
