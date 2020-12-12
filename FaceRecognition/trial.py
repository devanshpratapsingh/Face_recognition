import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    #Capture frame-by-frame
    ret, frame = cap.read()

    #Displaying the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
