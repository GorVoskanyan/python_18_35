class Person:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.isalpha():
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age


person = Person(name='Alex', age=20)
# person.set_name('Bob')
# print(person.get_name())

print(person.name)
person.name = '214332'
print(person.name)
