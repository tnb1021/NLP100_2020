import pandas as pd


df = pd.read_csv('data.txt',header=None,delimiter='\t')

result = df.sort_values(2)
print(result.head(5))

'''
         0  1     2     3
9    Sarah  F  1288  1880
29   Alice  F  1308  1881
8   Bertha  F  1320  1880
28  Bertha  F  1324  1881
27   Annie  F  1326  1881
'''