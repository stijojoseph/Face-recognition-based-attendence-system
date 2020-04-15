import os
import excel as r
def check(d):
 s=[]
 h=""
 i=0   
 listing = os.listdir(d+"/")
 for file in listing:

   f=str(file)
   print(file)
   for k in f:
    if k=='.':
        break
    h=h+k
   print(h)
   for k in f:
    if k==".":
         i=1
    if i>=1 and k=="j":  
     i=i+1
    if i>=1 and k=="p":  
     i=i+1
    if i>=1 and k=="g":  
     i=i+1
    if i==4:
      s.append(h)
      h=""
      i=0 
 
    
 print(s)
 r.names(s,d)
#check("classa")      