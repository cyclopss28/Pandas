import pandas as pd
import numpy as np
a = {'col1':[1,2],'col2':[3,4]}
info = pd.DataFrame(a)
print(info)
print(info.dtypes)
info.astype('int64').dtypes
info.astype({'col1':'int64'}).dtypes

