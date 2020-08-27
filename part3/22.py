import re
import json

f = open('jawiki-country.json','r',encoding='utf-8')
for line in f:
    f_data = json.loads(line)
    if f_data['title'] =='イギリス':
        target = f_data['text']
pattern = r'^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$'
result = re.findall(pattern,target,re.MULTILINE)
print('\n'.join(result))
print(result)
