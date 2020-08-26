import re
import json

f = open('jawiki-country.json','r',encoding='utf-8')
for line in f:
    f_data = json.loads(line)
    if f_data['title'] =='イギリス':
        target = f_data['text']
pattern = r'^(\[\[Category:.*\]\])$'
result = re.findall(pattern,target,re.MULTILINE)

print(result)
'''
['[[Category:イギリス|*]]', '[[Category:イギリス連邦加盟国]]', '[[Category:英連邦王国|*]]', '[[Category:G8加盟国]]', '[[Category:欧州連合加盟国|元]]', '[[Category:海洋国家]]', '[[Category:現存する君主国]]', '[[Category:島国]]', '[[Category:1801年に成立した国家・領域]]']
'''