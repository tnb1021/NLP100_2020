
results = []
with open('neko.txt.mecab',encoding='utf-8') as f:
    for line in f:
        surface = line.split('\t')
        if len(surface) == 2:
            attr = surface[1].split(',')
            result = {'surface':surface[0],'base':attr[6],'pos':attr[0],'pos1':attr[1]}
            results.append(result)

ans = set()

for i in range(2,len(results)):
    if results[i-2]['pos'] == '名詞' and results[i-1]['surface'] == 'の' and results[i]['pos'] == '名詞':
        ans.add(results[i-2]['surface']+results[i-1]['surface']+results[i]['surface'])

for i in range(10):
    print(list(ans)[i])

'''
以上の径路
妙齢の女子
リーシャスの援
主人の頭
自己の何
僕の翻訳
智慧の発達
時代の友達
同様の刑罰
博多の帯
'''
