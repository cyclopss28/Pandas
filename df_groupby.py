import pandas as pd
import numpy as np
data = {'Name':['Parker','Smith','William','John'],
        'Percentage':[82,98,91,87],
        'Course':['BSc','BEd','MPhill','BA']}
df = pd.DataFrame(data)
print(df)
grouped = df.groupby('Course')
print(grouped['Percentage'].agg(np.mean))

print(df.head(2))#prints first 2 rows
print(df.head(3))#prints first 3 rows