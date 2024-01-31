import pandas as pd
import numpy as np

a = pd.Series(['java','C','C++',np.nan])
a.map({'java':'core'})

