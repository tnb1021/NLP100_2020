import pandas as pd

df = pd.read_csv('data.txt',header=None,delimiter='\t')

df[0].to_csv('col1.txt',sep='\t',header=False,index=False)
df[1].to_csv('col2.txt',sep='\t',header=False,index=False)