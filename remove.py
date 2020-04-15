import os

def clean(d):
 i=0   
 listing = os.listdir(d+"/")
 for file in listing:
  #print(file)
  for k in file:
   if k==".":
         i=1
   if i>=1 and k=="n"or k=="d":  
    i=i+1
   if i>=1 and k=="p" or k=="a":  
    i=i+1
   if i>=1 and k=="y"or k=="t":  
    i=i+1
  if i==4:
      os.remove("/home/pi/AI_attendence/"+d+"/"+file)
      #print("file removed")
      i=0
      
    