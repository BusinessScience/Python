print("Hello")

for i in range(5,100):
    sum=0
    for j in range(1, i+1):
        if(i % j == 0):
            sum+= sum + 1
    if(i % 4 == 0):
        print(i)

for i in range(10,201):
    if(i == 3 or i == 5 or i == 100 or i == 150):
        continue
    else:
        print(i)

word = ("Enter a word: ")
first = 0
last = len(word)-1

is_palindrome = True
while(first <= last):
    if(word[first] != word[last]):
        is_palindrome = False
        break
    first += 1
    last -= 1

if(is_palindrome):
    print('jest')
else:
    print('nie')

lista = [1,2,3,4]
print(lista)

lista_2 = ["cos", True, 4]

print(lista_2)
print(lista_2[1])

lista_2.append(5)
print(lista_2)
print(lista_2[-2])
print(len(lista_2)/ 2)
print(len(lista_2)// 2)

lista_3 = []
lista_3_size = int(input("Wielkośc listy "))

for i in range(0, lista_3_size):
    elem = int(input('Podaj liczbę'))
    lista_3.append(elem)

print(lista_3)
lista_3.reverse()
print(lista_3)
print(lista_3[::-1])
print(lista_3)

n_lista = list(map(lambda x : x *2, lista_3))
print(n_lista)

lista_4 = [None] * 4
sum_1 = 0
for i in range(len(lista_4)):
    liczba = int(input("Podaj"))
    sum_1 += liczba

print(sum_1)

nn_list = []
for i, v in enumerate(lista_3):
    nn_list.append(v)

print(nn_list)

m_list = [f'indeks: {i}, element: {element}' for i, element in enumerate(lista_3)]
print(m_list)

import random
lotto = []
while len(lotto) < 6:
    numeber = random.randint(1, 49)
    if numeber not in lotto:
        lotto.append(numeber)

lotto.sort()
print(lotto)