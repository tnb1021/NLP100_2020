_str = "Hi He Lied Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

ans = {} #辞書の生成
_list = _str.split() #単語ごとのリスト
target = [1,5,6,7,8,9,15,16,19]

for i,word in enumerate(_list): #iにはインデックス番号(0,1,...)、wordにはオブジェクトが入る
    if i + 1 in target:
        ans[word[0]] = i + 1 #{単語の1文字目:インデックス番号+1(=何単語目か)}
    else:
        ans[word[:2]] = i + 1

print(ans) #{'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}

