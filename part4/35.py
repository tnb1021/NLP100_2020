
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

for i in ans[:20]:
    print(i)

'''
('の', 9194)
('て', 6868)
('は', 6420)
('に', 6243)
('を', 6071)
('と', 5508)
('が', 5337)
('た', 3988)
('で', 3806)
('も', 2479)
('ない', 2390)
('だ', 2363)
('し', 2322)
('から', 2032)
('ある', 1728)
('な', 1613)
('ん', 1568)
('か', 1530)
('いる', 1249)
('事', 1207)
'''