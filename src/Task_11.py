print(len('cos'))

a = "212365"
flag = True

if len(a) == 6 and a[2] == '-':
    for i in range(6):
        if i==2:
            continue
        if a[i].isdigit():
           flag = True
        else:
            flag = False
            break
else:
    flag=False

print(flag)

for i in range(1,100):
    if i==5 or i==50 or i==80:
        continue
    else:
        print(i)

b = 'kajoak'
c = (b[::1] == b[::-1])
print(c)

lista = ['gg', 'll', 'kk','ww']
lista.append('cc')
print(lista)
lista.insert(2,'zz')
print(lista)
lista[0] = 'oo'
print(lista)
print(lista[::-1])



import random

n = set()

while len(n) <6:
    nn = random.randint(1,51)
    n.add(nn)

n = list(sorted(n))
print(n)

dictt = {'kot':'cat', 'pies':'dog'}
print(dictt)
print(dictt['kot'])

kiss = dictt.keys()
print(kiss)
val = dictt.values()
print(val)

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [4,5,6]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('WYKRES')
plt.show()

x1 = []
y1 = []

for i in range(-5,6):
    x1.append(i)
    y1.append(i*3+1)

plt.plot(x1,y1)
plt.xlabel('x1')
plt.ylabel('y1')
plt.title('y = 3x + 1')
plt.show()

x2 = list(range(-5,5))
y2 = [x*2+20 for x in x2]

plt.plot(x2,y2, color='red')
plt.grid(True)
plt.show()

def sub(a,b):
    return a-b

print(sub(b=3, a=5))


























