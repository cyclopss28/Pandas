import pandas as pd
import numpy as np
print(pd.unique(pd.Series([2,1,3,3])))
print(pd.unique(pd.Series([pd.Timestamp('20160101'),
pd.Timestamp('20160101')])))
