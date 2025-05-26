file = open('file.txt', 'r')
read_file = file.read()
dict = {}
for letter in read_file:
    if letter.isalpha():
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

for letter in dict:
    print(letter, dict[letter])
