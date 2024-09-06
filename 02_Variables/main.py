"""Lesson1.
About variables and basic data types
"""

# Variables

# Don't use !#@!$%^&*()_+
# name1 = 'Gor'
# name_surname = 'Gor Voskanian'  # snake case
# nameSurname = 'Gor Voskanian'   # camel case
# NameSurname = 'Gor Voskanian'   # pascal case

# string <class 'str'>
# name = 'Gor'
# string_number = '7'
# print(type(string_number))

# single and double quotes
# text = 'I\'m fine'
# text = "I'm fine"
# text = "He said \"ok\""
# text = 'He said "ok"'
# print(text)

# long_text = '''Hello
# World
# !'''

# print(long_text)

# variable nameing
# fullname = 'Gor Voskanian'
# address = 'Hanrapetutyan 22'
# email = 'example@gmail.com'
# phone = '+37491112233'
# profession = 'Python Developer'
# age = 27

# case sensetive
# name = 'Gor'
# Name = 'Sergey'
# NAME = 'Alex'
# print(name)
# print(Name)
# print(NAME)

# ASCII table
# print(ord('Ա'))
# print(chr(1330))


# int, float, complex
# age = 27
# print(type(age))
# price = 27.99
# print(type(price))
# c = 27j
# print(type(c))

# convert
# age = float(age)
# print(type(age))
# print(age)

# price = int(price)
# print(price)
# print(type(price))

# age = str(age)
# print(age)
# print(type(age))


# baisc data types
age = 27
price = 27.0
text = 'hello'
is_student = True   # or False

# print(type(is_student))

# indexing of sequence
# first_letter = text[0]
# print(first_letter)
# last_char = text[-1]
# print(last_char)


# input() -> str function
# year_of_birth = float(input('Enter year of birth: '))
# age = 2024 - year_of_birth
# print(age)


# syntax basics
# print('Hello World!')

# number = int(input('Enter number: '))
# print(3 - number)


# concatenation
# a = '7'
# b = 8
# print(a + ' ' + '-' + ' ' + b)
# print(type(a * b))

city_1 = input('>>> ')
city_2 = input('>>> ')
result = city_1 + ' - ' + city_2
print(result)