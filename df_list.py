import pandas as pd
import numpy as np

''' x = ['pandas','python']
df = pd.DataFrame(x)
print(df) '''

#dataframe using arrays
info = {'ID':[101,102,103,104,105,106],
        'Department':['B.Sc','B.Tech','M.Tech','M.Sc','B.A.','B.Com']}
df = pd.DataFrame(info)
print(df)
#selecting single coloumn

print(df['ID'])

#adding a new coloumn in dataframe
df['Rollno.']=pd.Series([20,30,40])
print(df)

#deleting coloumn
del df['Rollno.']
print(df)

#Selection of single row in a DF
print(df.loc[4])
print(df.loc[3])

#selection of row by integer
print(df.iloc[0])

#selecting multiple rows using :
print(df[1:5])

#adding rows using append
''' info2 = pd.DataFrame([107], columns = ['ID'])
df = df.append(info2)
print(df) '''

df = df.drop(0)
print(df)