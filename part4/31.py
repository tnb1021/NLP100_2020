
results = []
with open('neko.txt.mecab',encoding='utf-8') as f:
    for line in f:
        surface = line.split('\t')
        if len(surface) == 2:
            attr = surface[1].split(',')
            result = {'surface':surface[0],'base':attr[6],'pos':attr[0],'pos1':attr[1]}
            results.append(result)

ans = set()
for target in results:
    if target['pos'] == '動詞':
        ans.add(target['surface'])

for i in range(10):
    print(list(ans)[i])

'''
泣かせ
洩り
睡ら
挟ん
繰り返し
撓り
通そ
縊れる
踏み込ん
攻め
'''
