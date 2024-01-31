import pandas as pd
import numpy as np
info = pd.DataFrame(np.random.randn(4,2),columns = ['col1','col2'])
for row_index, row in info.iterrows():
    print(row_index, row)