import cv2
import numpy as np

def empty(a):
    pass

cap = cv2.VideoCapture('http://192.168.250.188:4747/video')
# cap = cv2.VideoCapture(0)

cv2.namedWindow('HSV')
cv2.resizeWindow('HSV',800,440)

cv2.createTrackbar('min_hue','HSV',0,179,empty)
cv2.createTrackbar('max_hue','HSV',179,179,empty)

cv2.createTrackbar('min_sat','HSV',0,255,empty)
cv2.createTrackbar('max_sat','HSV',255,255,empty)

cv2.createTrackbar('min_val','HSV',0,255,empty)
cv2.createTrackbar('max_val','HSV',255,255,empty)

while True:
    c,frame  = cap.read()
    frame = frame[:280,88:510]
    frame = cv2.GaussianBlur(frame,(5,5),0)
    # frame = cv2.imread('orange_lambo.png')
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('min_hue','HSV')
    h_max = cv2.getTrackbarPos('max_hue','HSV')

    sat_min = cv2.getTrackbarPos('min_sat','HSV')
    sat_max = cv2.getTrackbarPos('max_sat','HSV')

    val_min = cv2.getTrackbarPos('min_val','HSV')
    val_max = cv2.getTrackbarPos('max_val','HSV')

    lower_range = np.array([h_min,sat_min,val_min])
    upper_range = np.array([h_max,sat_max,val_max])

    mask = cv2.inRange(hsv_frame,lower_range,upper_range)
    result = cv2.bitwise_and(frame,hsv_frame,mask=mask)

    cv2.imshow('s',hsv_frame)
    cv2.imshow('org',result)
    cv2.imshow('masked',mask)
    if cv2.waitKey(1)==ord('q'):
        break