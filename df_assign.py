import pandas as pd
import numpy as np
info = pd.DataFrame()
info ['ID'] = ['101','102','103']
print(info)

print(info.assign(Name = ['Smith','Parker','John']))
