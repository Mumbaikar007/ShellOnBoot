

import cv2
import datetime

cap = cv2.VideoCapture(0)

now = datetime.datetime.now()
print (now)

read, frame = cap.read()

cv2.imwrite('/home/optimus/'+ str(now) +'HAHA.jpg', frame)

cap.release()

