
import cv2
import numpy as np

pedistrian_detector = cv2.CascadeClassifier('Haarcascades\haarcascade_fullbody.xml')

cap = cv2.VideoCapture('walking.avi')

while (cap.isOpened()):

    ret, frame = cap.read()
    #frame = cv2.resize ( frame, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('Peds', gray)

        pedistrians = pedistrian_detector.detectMultiScale( gray, 1.05, 5)

        print ( len(pedistrians))
        for (x, y, w, h) in pedistrians:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        cv2.imshow('Pedistrians', frame)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()