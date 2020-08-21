import pandas as pd
import sys

args = sys.argv
n = int(args[1])
df = pd.read_csv('data.txt',header=None,delimiter='\t')

target = [i+i*df.shape[0]//n for i in range(n)]
result = [df[j:j+df.shape[0]//n+1] for j in target]

print(target) #[0, 557, 1114, 1671, 2228]
print(result)
