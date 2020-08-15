import pandas as pd

df = pd.read_csv('data.txt',header=None,delimiter='\t')
print(df.shape[0]) #2780
print(df.shape[1]) #4
