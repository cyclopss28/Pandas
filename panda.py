import pandas as pd
import numpy as np
'''creating series with arrays'''
info1 = np.array(['p','a','n','d','a'])
a = pd.Series(info1)
print(a)

'''create a series from dict'''
info2 = {'x':1, 'y':2,'z':3}
b = pd.Series(info2)
print(b)

'''create a series using scaler'''
x = pd.Series(4, index=[0,1,2,3,4])
print(x)