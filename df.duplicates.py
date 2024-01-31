import pandas as pd
import numpy as np
emp = {"Name":['Parker','Smith','William','Parker','Smith'],
       "Age":['21','32','29','21','32']}
info = pd.DataFrame(emp)
print(info)
print(info.drop_duplicates())
