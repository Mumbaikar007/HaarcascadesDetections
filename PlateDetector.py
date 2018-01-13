
import cv2
import numpy as np

plate_detector = cv2.CascadeClassifier( 'Haarcascades/haarcascade_licence_plate_rus_16stages.xml')

image = cv2.imread( 'rusplate2.jpg' )
gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)

plates = plate_detector.detectMultiScale ( gray, 1.1, 4)


for i in  plates:
    cv2.rectangle( image, ( i[0], i[1]), ( i[0]+i[2], i[0]+i[3]), ( 0, 255, 0), 2)

cv2.imshow( 'Plate', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
