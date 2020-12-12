import os
from PIL import  Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Images")

y_label = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jfif") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace("","").lower()
            print(label, path)
            #y_label.append(label)
            #x_train.append(path)
            pil_image = Image.open(path).convert("L")#grayscale
            image_array = np.array(pil_image, "uint8")
            print(image_array)


