
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

image = cv2.imread ('Drawung.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale ( gray, 1.05, 5)
print ( faces)
print (  faces[0][0] )

if faces is ():
    print( "No faces" )

for ( x, y, w, h ) in faces:

    cv2.rectangle( image, (x, y), (x + w, y + h), ( 0, 255, 0), 2 )
    cv2.imshow( 'Face', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

