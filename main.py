from PIL import Image, UnidentifiedImageError
import os
import cv2
import numpy as np

def get_image_data():
    paths = [os.path.join('jones_gabriel', f)
             for f in os.listdir('jones_gabriel')
             if not f.startswith('.')]  # Skip hidden files
    faces = []
    ids = []
    for path in paths:
        try:
            image = Image.open(path).convert('L')
            image_np = np.array(image, 'uint8')
            id = int(path.split('.')[1])

            ids.append(id)
            faces.append(image_np)
        except UnidentifiedImageError:
            print(f"Skipped {path} because it's not a recognized image format.")
            continue  # Skip this file and move on to the next one

    return np.array(ids), faces


ids, faces = get_image_data()


lbph_classifier = cv2.face.LBPHFaceRecognizer_create()
lbph_classifier.train(faces, ids)
lbph_classifier.write('lbph_classifier.yml')