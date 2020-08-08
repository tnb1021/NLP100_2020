_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

_str = _str.replace(',','').replace('.','') #,と.を削除する
print(_str) #Now I need a drink alcoholic of course after the heavy lectures involving quantum mechanics

_list = _str.split()
print(_list) #['Now', 'I', 'need', 'a', 'drink', 'alcoholic', 'of', 'course', 'after', 'the', 'heavy', 'lectures', 'involving', 'quantum', 'mechanics']

ans = [len(i) for i in _list]
print(ans) #[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]