str_1 = "パトカー"
str_2 = "タクシー"

ans_1 = ''.join([i+j for i,j in zip(str_1,str_2)]) 
print(ans_1) #パタトクカシーー

_list = []
for i,j in zip(str_1,str_2):
    _list.append(i+j)
ans_2 = ''.join(_list)
print(ans_2) #パタトクカシーー