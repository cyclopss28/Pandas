import pandas as pd
import numpy as np
info= pd.DataFrame({'a_data': [45, 28, 39, 32, 18],  
'b_data': [26, 37, 41, 35, 45],  
'c_data': [22, 19, 11, 25, 16]})  
print(info)
print(info.shift(periods=2))
print(info.shift(periods=2, axis=1))