import pandas as pd
import numpy as np
info = pd.DataFrame({'X': range(1, 6),  
                    'Y': range(10, 0, -2),  
                    'Z Z': range(10, 5, -1)})  

info.query('X > Y')
info[info.X > info.Y]
info(info.Y == info['Z Z'])
