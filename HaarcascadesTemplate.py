
import cv2
import numpy as np

classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_fullbody.xml')

image = cv2.imread ('peds.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

haarcascades = classifier.detectMultiScale ( gray, 1.05, 5)
print ( haarcascades )
print (  haarcascades[0][0] )

if haarcascades is ():
    print( "No faces" )

for ( x, y, w, h ) in haarcascades:

    cv2.rectangle( image, (x, y), (x + w, y + h), ( 0, 255, 0), 2 )
    cv2.imshow( 'Haarcascades', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

