import cv2
import os
from PIL import  Image
import numpy as np
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Images")

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_label = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jfif") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace("","").lower()
            #print(label, path)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            #print(label_ids)
            #y_label.append(label)
            #x_train.append(path)
            pil_image = Image.open(path).convert("L")#grayscale
            image_array = np.array(pil_image, "uint8")
            #print(image_array)
            faces = face_classifier.detectMultiScale(image_array, 1.5, 5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_label.append(id_)


print(y_label)
print(x_train)

with open("labels.pickle","wb") as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_label))
recognizer.save("trainer.yml")
