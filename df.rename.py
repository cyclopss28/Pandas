import pandas as pd
import numpy as np
info = {'name': ['Parker', 'Smith', 'William', 'Robert'],   
              'age': [38, 47, 44, 34],   
               'language': ['Java', 'Python', 'JavaScript', 'Python']}   
info_pd = pd.DataFrame(info)
print(info_pd.columns)
info_pd.rename(columns = {'name':'Name','age':'Age','language':'Language'}, inplace=True)
print(info_pd)
print(info_pd.columns)