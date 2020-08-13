#英小文字の文字コードの範囲を確認
print(ord('a'),ord('z')) #97 122

def cipher(text):
    result = []
    for i in text:
        if i.islower():
            result.append(chr(219-ord(i)))
        else:
            result.append(i)
    return ''.join(result)

test_txt = "I have a pen."
ans = cipher(test_txt)
print('暗号化:',ans) #暗号化: I szev z kvm.
ans = cipher(ans)
print('復号化:',ans) #復号化: I have a pen.
