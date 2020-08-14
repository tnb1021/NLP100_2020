import random

def typo(word):
    if len(word) >= 5:
        word = [word[0]] + random.sample(word[1:-1],len(word[1:-1])) + [word[-1]]
    return ''.join(word)
target = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = [typo(i) for i in target.split()]
print(ans) #['I', 'condul’t', 'bieevle', 'that', 'I', 'cuold', 'aluactly', 'udaersntnd', 'what', 'I', 'was', 'reaindg', ':', 'the', 'pemnaoenhl', 'pweor', 'of', 'the', 'haumn', 'mind', '.']
print(' '.join(ans)) #I condul’t bieevle that I cuold aluactly udaersntnd what I was reaindg : the pemnaoenhl pweor of the haumn mind .