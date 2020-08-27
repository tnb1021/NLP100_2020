import re
import json

f = open('jawiki-country.json','r',encoding='utf-8')
for line in f:
    f_data = json.loads(line)
    if f_data['title'] =='イギリス':
        target = f_data['text']
pattern = r'^(=+)([^=]+)(=+)$'
result = re.findall(pattern,target,re.MULTILINE)

print(','.join(i[1] + ':' + str(len(i[0])-1) for i in result))
'''
国名:1,歴史:1,地理:1,主要都市:2,気候:2,政治:1,元首:2,法:2,内政:2,地方行政区分:2,...
'''
