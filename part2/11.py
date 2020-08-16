import pandas as pd

df = pd.read_csv('data.txt',header=None,delimiter='\t')
df.to_csv('newdata.txt',sep=' ',header=False,index=False)