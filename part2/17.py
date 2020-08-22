import pandas as pd


df = pd.read_csv('data.txt',header=None,delimiter='\t')

print(df[0].duplicated().value_counts())
print(df[0].unique())
print(df[0].nunique())

'''
True     2644
False     136
Name: 0, dtype: int64
['Mary' 'Anna' 'Emma' 'Elizabeth' 'Minnie' 'Margaret' 'Ida' 'Alice'
 'Bertha' 'Sarah' 'John' 'William' 'James' 'Charles' 'George' 'Frank'
 'Joseph' 'Thomas' 'Henry' 'Robert' 'Annie' 'Edward' 'Clara' 'Florence'
 'Ethel' 'Bessie' 'Harry' 'Helen' 'Ruth' 'Marie' 'Lillian' 'Mildred'
 'Dorothy' 'Frances' 'Walter' 'Evelyn' 'Virginia' 'Richard' 'Betty'
 'Donald' 'Doris' 'Shirley' 'Barbara' 'Patricia' 'Joan' 'Nancy' 'Carol'
 'David' 'Ronald' 'Judith' 'Linda' 'Sandra' 'Carolyn' 'Sharon' 'Michael'
 'Susan' 'Donna' 'Larry' 'Kathleen' 'Deborah' 'Gary' 'Karen' 'Debra'
 'Pamela' 'Cynthia' 'Mark' 'Steven' 'Lisa' 'Jeffrey' 'Lori' 'Kimberly'
 'Tammy' 'Angela' 'Michelle' 'Jennifer' 'Melissa' 'Christopher' 'Brian'
 'Amy' 'Laura' 'Tracy' 'Julie' 'Jason' 'Scott' 'Stephanie' 'Heather'
 'Nicole' 'Matthew' 'Rebecca' 'Jessica' 'Amanda' 'Daniel' 'Kelly' 'Joshua'
 'Crystal' 'Ashley' 'Megan' 'Brittany' 'Andrew' 'Justin' 'Samantha'
 'Lauren' 'Emily' 'Brandon' 'Tyler' 'Taylor' 'Nicholas' 'Jacob' 'Hannah'
 'Austin' 'Alexis' 'Rachel' 'Madison' 'Abigail' 'Olivia' 'Ethan' 'Anthony'
 'Isabella' 'Ava' 'Sophia' 'Chloe' 'Alexander' 'Mia' 'Jayden' 'Noah'
 'Aiden' 'Mason' 'Liam' 'Charlotte' 'Harper' 'Benjamin' 'Elijah' 'Amelia'
 'Logan' 'Oliver' 'Lucas']
136
'''