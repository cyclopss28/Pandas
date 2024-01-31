import pandas as pd
import numpy as np

#create df using dict

info1 = pd.DataFrame({"x":[25,15,12],
                     "y":[47,24,17]})
info2 = pd.DataFrame({"z":[38,12,45]})

print(info1)
print(info2)

print(info1._append(info2, ignore_index = True))
print(info1.describe())