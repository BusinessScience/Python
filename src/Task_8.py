class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Jan', 20)
person2 = Person('Tom', 22)
person3 = Person('Kate', 23)
print(person.name)
print(person.age)
print(person.age, person.name)
print('\n\n')

people = [person, person2, person3]
#people.append(person)
#people.append(person2)
#people.append(person3)


for person in people:
    if person.age > 20:
        print(person.name)