import pandas as pd


df = pd.read_csv('data.txt',header=None,delimiter='\t')

print(df[0].value_counts().head(10))

'''
James        118
William      111
John         108
Robert       108
Mary          92
Charles       75
Michael       74
Elizabeth     73
Joseph        70
Margaret      60
Name: 0, dtype: int64
'''