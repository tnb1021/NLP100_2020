import re
import json

f = open('jawiki-country.json','r',encoding='utf-8')
for line in f:
    f_data = json.loads(line)
    if f_data['title'] =='イギリス':
        target = f_data['text']

pattern = r'\|(.+?)\s=\s*(.+)'
result = dict(re.findall(pattern,target,re.MULTILINE))

result_s = {}
for i,j in result.items():
    #強調
    pattern = r'\'{2,5}'
    match = re.sub(pattern,'',j)
    
    #内部リンク
    pattern = r'\[\[(.+\|)?(.+?)\]\]'
    match = re.sub(pattern,'\2',j)
    
    #外部リンク
    pattern = r'\[\[(.+\|)?(.+?)\]\]'
    match = re.sub(pattern,'\2',j)

    #htmlタグ
    pattern = r'<.+?>'
    match = re.sub(pattern,'',j)

    result_s[i] = match
print(result_s)
