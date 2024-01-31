import pandas as pd
import numpy as np

info = pd.DataFrame([[2,7]]*4, columns = ['P','Q'])
info.apply(np.sqrt)
info.apply(np.sum, axis = 0)
info.apply(np.sum, axis = 1)
info.apply(lambda x:[1,2], axis = 1)
info.apply(lambda x:[1,2], axis = 1, result_type='expand')
info.apply(lambda x: pd.Series([1,2], index=['foo','bar']), axis = 1)
info.apply(lambda x:[1,2], axis = 1, result_type='broadcast')
print(info)

