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
for result in results:
    if result['pos'] != '記号':
        if result['surface'] not in ans:
            ans[result['surface']] = 0
        ans[result['surface']] += 1
ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)    

x = range(1,len(ans)+1)
y = [i[1] for i in ans]
plt.scatter(x,y) #散布図
plt.xscale('log') #スケールをlogにする
plt.yscale('log')
plt.show()