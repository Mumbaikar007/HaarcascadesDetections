
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')


image = cv2.imread ('Trump.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale ( gray, 1.05, 5)

if faces is ():
    print( "No faces" )

for ( x, y, w, h ) in faces:

    cv2.rectangle( image, (x, y), (x + w, y + h), ( 0, 255, 0), 2 )
    cv2.imshow( 'Face', image)
    cv2.waitKey(0)

    roi_gray = gray[y:y+h, x:x+w]
    roi_image = image[y:y+h, x:x+w]

    eyes = eye_classifier.detectMultiScale ( roi_gray, 1.05, 4)

    for ( ex, ey, ew, eh) in eyes:

        cv2.rectangle( roi_image, ( ex, ey), (ex+ew, ey+eh), (0,0,255), 3)
        cv2.imshow( 'Face', image)
        cv2.waitKey(0)

cv2.destroyAllWindows()

