import face_recognition
import cv2
import numpy as np
from PIL import Image,ImageDraw
import pickle

all_face_encodings = {}

shah_image = face_recognition.load_image_file("std/alexa.jpg")
np.save("std/shah",shah_image)


shah_encoding = face_recognition.face_encodings(shah_image)[0]
np.save("std/shah-en",shah_encoding)
