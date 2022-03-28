import mediapipe as mp
import cvzone
import cv2
import numpy as np

cap = cv2.VideoCapture('http://192.168.43.254:4747/video')

while True:
    success , frame = cap.read()

    low_rng = (50,0,78)
    up_rng = (130,255,255)
    
    frame = frame[:280,88:510]
    f_cp = frame.copy()

    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(hsv_frame,low_rng,up_rng)

    img = cv2.imread('orange_lambo.png')
    img = cv2.resize(img,(422,280))
    # gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    imgclr , contour = cvzone.findContours(frame,mask,minArea=800)
    if contour:
        x,y,w,h = contour[0]['bbox']
        # cv2.circle(frame,(x,y+h),5,(255,0,0),cv2.FILLED)
        # cv2.circle(img,(x,y),5,(255,0,0),cv2.FILLED)
        frame[y:y+h,x:x+w] = img[y:y+h,x:x+w]
        cv2.putText(frame,'You are wrong',(100,180),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,250),3)
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    # cv2.imshow('img clr',img)
    cv2.putText(f_cp,'Is there any car image ?',(30,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,240),2)
    cv2.imshow('img ',frame)
    cv2.imshow('img_c ',f_cp)

    if cv2.waitKey(1) == ord('q'):
        break