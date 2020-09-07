
results = []
with open('neko.txt.mecab',encoding='utf-8') as f:
    for line in f:
        surface = line.split('\t')
        if len(surface) == 2:
            attr = surface[1].split(',')
            result = {'surface':surface[0],'base':attr[6],'pos':attr[0],'pos1':attr[1]}
            results.append(result)

ans = set()
temp = []
for result in results:
    if result['pos'] == '名詞':
        temp.append(result['surface'])
    elif len(temp) >= 2:
        ans.add(''.join(temp))
        temp = []
    else:
        temp = []

for i in range(10):
    print(list(ans)[i])

'''
事六十年前これ
弁難攻撃
甚兵衛君
美学者迷亭先生
世界何億万
三平君今日
関係上三介
鉄拳制裁
金満家
運動律
'''