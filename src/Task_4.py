
def add(a,b):
    return a + b

sum = add(4,5)
print(add(5,6))
print(sum)


def sub(x,y):
    return x - y

print(sub(4,5))


x = 5
y = 7
print(sub(x,y))
print('Róznica liczb to: ', sub(x,y))
print('Suma liczb to: ', add(a=x, b=y))

def function_args(**argumnts):
    print(argumnts['x'])
    print(argumnts['y'])

function_args(x=234, y=345)

#dict
def my_function_dict(**args):
    print(args)

my_function_dict(name='Anna', age=30, active=True)

#list
def my_function_list(*args):
    print('czy działa?')
    for arg in args:
        print(arg)

m_lista = [1,5,3,4,5,63,2,4,2,3]
m_lista.sort()
my_function_list(m_lista)

def is_even_number(x):
    if x % 2 == 0:
        print('Jest parzysta')
        return True
    else:
        print('Nieparzysta')
        return False

is_even_number(578)

from Task_1 import my_dict as md

print(md.my_dict)

