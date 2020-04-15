from PIL import Image
import face_recognition
import numpy as np
import cv2
import os
import excel as e


def extract(k):
 name=[]
 i=1   
 image=face_recognition.load_image_file(k+'.jpg')
 import os
 img=cv2.imread(k+".jpg",1)
 cv2.imshow("test",img)
 cv2.waitKey(2000)
 cv2.destroyAllWindows()
 
 face_locations=face_recognition.face_locations(image)
 for face_location in face_locations:
    print("Face",i,"extraction process starting[###",end="")
   
    top,right,bottom,left=face_location
    print("#",end ="")
    face_image=image[top:bottom,left:right]
    print("#",end ="")
    pil_image=Image.fromarray(face_image)
    print("#",end ="")
 #   pil_image.show()
 #   k=input("enter the face name")
    #cv2.destroyAllWindows()
    #cv2.waitKey(0)
    print("####",end ="")
    img = np.array(pil_image)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print("###",end ="")
   # scale_percent = 60 # percent of original size
    #width = int(img.shape[1] * scale_percent / 100)
    #height = int(img.shape[0] * scale_percent / 100)
    #dim = (width, height)
    #img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("test",img)
    print("####",end ="")
    cv2.waitKey(1000)
    print("###]finished\n\n\n")
    y=input("Type the student name :-")
    name.append(y)
    cv2.destroyAllWindows  
    pil_image.save(k+"/"+str(y)+'.jpg')
    i=i+1
 e.names(name,k)
 print("CSV file created and saves as",k+"attendence.csv")