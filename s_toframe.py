import pandas as pd
import numpy as np
''' s = pd.Series(["a","b","c"],
              name = "vals")
print(s.to_frame()) '''

emp = ['Parker','John','Smith','William']
id = [102,107,109,114]
emp_series = pd.Series(emp)
id_series = pd.Series(id)
frame = {'Emp':emp_series, 'ID':id_series}
result = pd.DataFrame(frame)
print(result)