import pandas as pd
import sys

args = sys.argv
df = pd.read_csv('data.txt',header=None,delimiter='\t')

n = int(args[1])

print(df.head(n)) #n=2

'''
      0  1     2     3
0  Mary  F  7065  1880
1  Anna  F  2604  1880
'''