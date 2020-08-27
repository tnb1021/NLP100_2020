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
'''
イギリス
イギリス連邦加盟国
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
現存する君主国
島国
1801年に成立した国家・領域
'''
