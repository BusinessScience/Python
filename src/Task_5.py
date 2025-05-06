def is_pesel(pesel):
    if pesel.isdigit() and len(pesel) == 11:
        print(pesel, 'Is pesel')
        return True
    else:
        print(pesel, 'Is not pesel')
        return False

pesel = input('Enter pesel: ')
is_pesel(pesel)

import math

boolean = math.isqrt(5)
print(float(math.isqrt(5)))
print(boolean)

number = int(input('Enter number: '))

if (math.isqrt(number) * math.isqrt(number) == number):
    print(True)
else:
    print(False)

def find_next_integer(lista):
    a = set(lista)
    for i in range(1,len(a)+2):
        if i not in a:
            return i

print(find_next_integer([1,2,3,5]))