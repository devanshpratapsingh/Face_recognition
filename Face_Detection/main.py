import cv2

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = face_classifier.detectMultiScale(gray,1.1,4)



cv2.imshow('img', img)
cv2.waitKey()
