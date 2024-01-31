import pandas as pd
import numpy as np
info=pd.DataFrame(np.random.randn(10,2),index=[1,3,7,2,4,5,9,8,0,6],columns=['col2','col1'])  
print(info)
info2 = info.sort_index()
print(info2)
info3 = info2.sort_index(ascending=False)
print(info3)
info3 = info2.sort_index(axis=1)
print(info3)
info3 = info2.sort_values(by='col2')
print(info3)