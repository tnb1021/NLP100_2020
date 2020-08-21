import pandas as pd
import sys

args = sys.argv
n = int(args[1])
df = pd.read_csv('data.txt',header=None,delimiter='\t')

result = [df[i:i+df.shape[0]//n] for i in range(n)]
print(result)