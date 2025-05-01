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

word = input("Enter a word: ")
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
