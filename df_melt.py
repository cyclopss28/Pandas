import pandas as pd
import numpy as np
info = pd.DataFrame({'Name': {0: 'Parker', 1: 'Smith', 2: 'John'},   
                   'Language': {0: 'Python', 1: 'Java', 2: 'C++'},   
                   'Age': {0: 22, 1: 30, 2: 26}})   
  
# Name is id_vars and Course is value_vars   
print(pd.melt(info, id_vars =['Name'], value_vars =['Language']))   
print(info)  