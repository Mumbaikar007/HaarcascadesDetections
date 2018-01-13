

import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while (True):

    ret, frame = cap.read()

    faces = face_classifier.detectMultiScale ( cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY), 1.05, 5)

    for ( x, y, w, h ) in faces:
        cv2.rectangle( frame, (x, y), (x + w, y + h), ( 0, 255, 0), 2 )


    cv2.imshow( 'Face', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

