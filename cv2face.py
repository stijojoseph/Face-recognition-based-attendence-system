import face_recognition
import cv2
import numpy as np
from PIL import Image,ImageDraw
import pickle

all_face_encodings = {}

shah_image = face_recognition.load_image_file("alexa.jpg")
np.save("shah",shah_image)


shah_encoding = face_recognition.face_encodings(shah_image)[0]
np.save("shah-en",shah_encoding)



all_face_encodings["shahrukhan"] = face_recognition.face_encodings(shah_image)[0]

with open('dataset_sali1.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)


known_face_encodings=[shah_encoding]
print(type(known_face_encodings))
known_face_names=["joe"]
test_image=face_recognition.load_image_file('stud2.jpeg')
face_locations=face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image,face_locations)
pil_image=Image.fromarray(test_image)
draw=ImageDraw.Draw(pil_image)
for (top,right,bottom,left) ,face_encoding in zip(face_locations,face_encodings):
    matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
    name="Unknown Person"
    if True in matches:
        first_match_index=matches.index(True)
        name=known_face_names[first_match_index]
    draw.rectangle(((left+2,top+2),(right+2,bottom+2)),outline=(0,255,255))
    text_width,text_height=draw.textsize(name)
    draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left+6,bottom-text_height-5),name,fill=(255,255,255,255))
del draw
img = np.array(pil_image)
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("test",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
