print(".....FACE RECOGNITION ATTENDENCE SYSTEM.....\n\n\n")

import attendencename as f
print("..##...CREDITS  STIJO JOSEPH .YOUTUBE.@ Electrical Coder...##..\n\n\n")
import attendencemain as d

import os
import manual as m
i=1

while i>0 and i<4:
    print("* Enter the number for the folllowing jobs\n")
    print("1.Automatic student photo Training data creation \n2.Manual student photo traing data creation ")
    print("3.Training and attendence testing \n")
    i=int(input("user input::-"))
    if i==1:
       k=input("Enter the Class Name")
       if not os.path.isdir(k):
        os.makedirs(k)
        print("new class created - : ", k) 
       else:
        print(k, " already exists.")        
       f.extract(k) 
    if i==3:
    
       k=input("Enter the Class Name \n")
       if not os.path.isdir(k):
        
        print(k,"doesnot exist make the class") 
       else:
        print(k, " already exists \n")   
        g=input("Give the .jpg filename for faces to be detected in\n")
        d.verify(k,g)
 
   
    if i==2:
       k=input("Enter the Class Name")
       if os.path.isdir(k):
        print(k, " already exists.")        
        m.check(k)
       else:
           print("........@#@# \nFolder not found...\n\n first create a folder in the name of the class and \n\nsave faces with their name as jpf file\n\n\n")