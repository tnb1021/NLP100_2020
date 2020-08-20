import pandas as pd
import sys

args = sys.argv
df = pd.read_csv('data.txt',header=None,delimiter='\t')
print(type(args[1])) #<class 'str'>
n = int(args[1])

print(df.tail(n)) #n=5

'''
             0  1      2     3
2775  Benjamin  M  13381  2018
2776    Elijah  M  12886  2018
2777     Lucas  M  12585  2018
2778     Mason  M  12435  2018
2779     Logan  M  12352  2018
'''