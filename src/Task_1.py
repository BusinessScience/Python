from operator import index

words_pl = ['kot', 'pies']
words_en = ['cat', 'dog']

word = input('podaj słowo po poslku')

try:
    index = words_pl.index(word)
    if word in words_pl:
        print(words_en[index])
except:
    print('nie znaleziono lub błąd danych')


my_dict = {'kot' : 'cat',
           'pies' : 'dog'}
if word in my_dict:
    print(my_dict[word])
else:
    print('not found')