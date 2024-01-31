import pandas as pd
import numpy as np
info = pd.DataFrame({'P': ['Smith', 'John', 'William', 'Parker'],   
      'Q': ['Python', 'C', 'C++', 'Java'],   
      'R': [19, 24, 22, 25]})   
table = pd.pivot_table(info, index = ['P','Q'])
print(table)