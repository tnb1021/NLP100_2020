import re
import json

f = open('jawiki-country.json','r',encoding='utf-8')
for line in f:
    f_data = json.loads(line)
    if f_data['title'] =='イギリス':
        target = f_data['text']
pattern = r'\[\[(ファイル|File):(.+?)\|'
result = re.findall(pattern,target,re.MULTILINE)

print(','.join(i[1] for i in result))
'''
Royal Coat of Arms of the United Kingdom.svg,Descriptio Prime Tabulae Europae.jpg,Lenepveu, Jeanne d'Arc au siège d'Orléans.jpg,
'''
