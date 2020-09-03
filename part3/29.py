import re
import json
import requests

f = open('jawiki-country.json','r',encoding='utf-8')
for line in f:
    f_data = json.loads(line)
    if f_data['title'] =='イギリス':
        target = f_data['text']
pattern = r'\|(.+?)\s=\s*(.+)'
result = dict(re.findall(pattern,target,re.MULTILINE))

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f"File:{result['国旗画像']}",
    "iiprop": "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
data_dict = DATA["query"]["pages"]["23473560"]["imageinfo"][0]
print(data_dict['url']) #https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg