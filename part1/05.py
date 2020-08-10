
def ngram(target,n):
    return [target[i:i+n] for i in range(len(target)-n+1)]

_str = "I am an NLPer"
word = _str.split()
print(word) #['I', 'am', 'an', 'NLPer']
char_bi_gram = ngram(_str,2)
word_bi_gram = ngram(word,2)

print('単語bi-gram:',word_bi_gram)
print('文字bi-gram:',char_bi_gram)
#単語bi-gram: [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
#文字bi-gram: ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']