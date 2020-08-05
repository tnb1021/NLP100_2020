_str = "stressed"

_list = list(reversed(_str)) #_list = ['d', 'e', 's', 's', 'e', 'r', 't', 's']
ans_1 = ''.join(_list) #結合

ans_2 = _str[::-1] #start: stop: step-1

print(ans_1,ans_2)