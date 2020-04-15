
import xlsxwriter 
# import xlsxwriter module
def names(names,r):
    

  
 import pandas as pd

# create dataframe
 df= pd.DataFrame({'name': names,'attendence':""
     })

 df.to_csv(r+"ATTENDENCE.csv") 
 print('Students names added to CSV files')