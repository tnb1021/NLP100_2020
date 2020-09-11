import matplotlib.pyplot as plt
import japanize_matplotlib

results = []
with open('neko.txt.mecab',encoding='utf-8') as f:
    for line in f:
        surface = line.split('\t')
        if len(surface) == 2:
            attr = surface[1].split(',')
            result = {'surface':surface[0],'base':attr[6],'pos':attr[0],'pos1':attr[1]}
            results.append(result)

ans = {}

for i in range(len(results)):
    if results[i]['surface'] == '猫':
        for j in range(11): #猫の前後5単語が対象
            if results[i-5+j]['pos'] != '記号' and results[i-5+j]['pos'] != '助詞' and results[i-5+j]['pos'] != '助動詞':
                if results[i-5+j]['surface'] not in ans:
                    ans[results[i-5+j]['surface']] = 0
                ans[results[i-5+j]['surface']] += 1

del ans['猫'] #猫の削除
ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)    

label = [i[0] for i in ans[:10]]
y = [i[1] for i in ans[:10]]
plt.bar(label,y)
plt.show()
print(ans)