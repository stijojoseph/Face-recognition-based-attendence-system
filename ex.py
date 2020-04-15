import pandas as pd
import xlsxwriter
import numpy as np
# create dataframe


def reads(r,v):
 m=0
 w=[]
   
 df = pd.read_csv(v+'ATTENDENCE.csv')
 #df['attendence']="present" 
 k=df['name'].tolist()
 h=df['attendence'].tolist()
 

 if k==r:
    # print("all are present")
     for r in k:
      df['attendence']="present"  
 else:
     i=0
     for f in k:
         for t in r:
             if f==t:
                 m=m+1
         #print(m,f)
         if m==0:
            # print(f)
             df.loc[df['name'] ==str(f), 'attendence'] = "absent"
             w.append(f)
         else:
             
             df.loc[df['name'] ==str(f), 'attendence'] = "present"
             m=0
         i=i+1      
 df.to_csv(v+"ATTENDENCE.csv",index=False)
 
 #print('DataFrame is written successfully to Excel File.')
 return w

   


 