import pandas as pd
import numpy as np
left = pd.DataFrame({  
   'id':[1,2,3,4],  
   'Name': ['John', 'Parker', 'Smith', 'Parker'],  
   'subject_id':['sub1','sub2','sub4','sub6']})  
right = pd.DataFrame({  
    'id':[1,2,3,4],  
   'Name': ['William', 'Albert', 'Tony', 'Allen'],  
   'subject_id':['sub2','sub4','sub3','sub6']})  

print (pd.merge(left, right, on ='id'))
