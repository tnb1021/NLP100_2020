module = __import__('05')

x = "paraparaparadise"
y = "paragraph"

X = set(module.ngram(x,2)) #set()で重複する要素を削除
Y = set(module.ngram(y,2))

#和集合
union_1 = X | Y
union_2 = X.union(Y) 

#積集合
intersection_1 = X & Y
intersection_2 = X.intersection(Y)

#差集合
difference_1 = X - Y
difference_2 = X.difference(Y)

#'se'があるか
ans_X = 'se' in X
ans_Y = 'se' in Y

print('X:',X)
print('Y:',Y)
print('和集合:',union_1,union_2)
print('積集合:',intersection_1,intersection_2)
print('差集合:',difference_1,difference_2)
print('"se"があるか,X:',ans_X,'Y:',ans_Y)
'''
X: {'ra', 'di', 'se', 'is', 'ad', 'ar', 'ap', 'pa'}
Y: {'ra', 'pa', 'ar', 'gr', 'ap', 'ph', 'ag'}
和集合: {'ag', 'ra', 'di', 'se', 'is', 'ad', 'ar', 'gr', 'ap', 'ph', 'pa'} 
{'ag', 'ra', 'di', 'se', 'is', 'ad', 'ar', 'gr', 'ap', 'ph', 'pa'}
積集合: {'ar', 'ra', 'ap', 'pa'} {'ar', 'ra', 'ap', 'pa'}
差集合: {'di', 'ad', 'se', 'is'} {'di', 'ad', 'se', 'is'}
"se"があるか,X: True Y: False
'''
