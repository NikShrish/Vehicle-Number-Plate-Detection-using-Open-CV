import numpy as np
import cv2

###########################################################################
framewidth=640
frameheight=480
nameplate=cv2.CascadeClassifier("resource\haarcascade_russian_plate_number.xml")
color=(255,0,0)
minarea=0
count=0
###########################################################################

cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(5,150)


while True:
    success,img=cap.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    namePlt=nameplate.detectMultiScale(imgGray,1.1,4)


    for (x,y,w,h) in namePlt:
        area=w*h
        if area > minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            roi=img[y:y+h,x:x+w]
            cv2.imshow("regions",roi)


    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF== ord('s'):
        cv2.imwrite("resource/Nameplates/scannedNameplates"+str(count)+" .jpg",roi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)   #feedback
        cv2.putText(img,"scan saved",(150,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),3)
        cv2.imshow("Result",img)
        cv2.waitKey(0)
        count +=1