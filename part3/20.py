import json

f = open('jawiki-country.json','r',encoding='utf-8')
for line in f:
    f_data = json.loads(line)
    if f_data['title'] =='イギリス':
        result = f_data['text']

print(result)