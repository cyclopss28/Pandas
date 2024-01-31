import pandas as pd
import numpy as np
info = pd.DataFrame({'Key':['K0','K1','K2','K3','K4','K5'],
                     'A':['A0','A1','A2','A3','A4','A5']})
x = pd.DataFrame({'Key':['K0','K1','K2'],
                  'B':['B0','B1','B2']})
info.join(x, lsuffix = '_caller', rsuffix = '_x')
info.set_index('Key').join(x.set_index('Key'))
print(info.join(x.set_index('Key'), on = 'Key'))
print(info)