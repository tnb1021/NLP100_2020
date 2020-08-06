_str = "パタトクカシーー"

_list = [_str[0],_str[2],_str[4],_str[6]] #1つ1つ取り出しリストへ格納
ans_1 = ''.join(_list)

ans_2 = _str[::2] #start: stop: step2

print(ans_1,ans_2) #パトカー パトカー