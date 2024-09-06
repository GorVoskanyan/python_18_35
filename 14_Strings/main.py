# strings

# index, slice
# text = 'python'
# first_char = text[0]
# last_char = text[-1]

# first_half = text[:len(text) // 2]
# second_half = text[len(text) // 2:]
# text_copy = text[:]

# print(text_copy)
# print(first_half)
# print(second_half)


# string methods
# fullname = input('Enter fullname: ').title()

# fullname = 'G' + fullname[1:]
# fullname = fullname.upper()
# fullname = fullname.lower()
# fullname = fullname.capitalize()
# fullname = fullname.title()

# import re
# print(help(re))

# fullname = input('Enter fullname: ')

# if fullname.islower():
#     print('Ok')

# if fullname.isupper():
#     print('Ok')

# if fullname.isdigit():
#     print('Ok')

# if fullname.isalnum():
#     print('Ok')

# print(fullname)


text = 'London is the capital of Great Britian'

# changed_text = text.replace('London is the', 'Yerevan')
# changed_text = text.replace('London', 'Yerevan')
# print(changed_text)

# words_list = text.split(' ')
# words_list = text.split()
# print(words_list)
# t = '-'.join(words_list)


# print(text.index('o'))
# print(text.index('o', 3))
# print(text.index('o', 2, 20))

# print(text.find('o'))
# print(text.find('o', 2))
# print(text.find('w', 2, 20))

# print(text.count('o'))

# text = text.strip()
# text = text.rstrip()
# text = text.lstrip()
# print(text)

# print(text.center(len(text) + 20, '-'))

# if text.startswith('London'):
#     print('Ok')

# if text.endswith('Britian'):
#     print('Ok')

# text.endswith()


# string formatting
# quantity = 5
# product = 'Iphone'
# price = 999.99

# res = str(quantity) + ' ' + product + ' ' + 'total price ' + str(price * quantity) + '$'
# res = '{} {} total price {}'.format(quantity, product, price*quantity)
# res = '{1} {0} total price {2}'.format(quantity, product, price*quantity)
# res = '{q} {p} total price {t}'.format(q=quantity, p=product, t=price*quantity)

# Python 3.6 +    f-string
# res = f"{quantity:04d} {product:^50} total price {(price*quantity):.2f}$"

# res = "%04d %s total price %.2f" % (quantity, product, price*quantity)
# print(res)


fullname = input('Enter fullname: ')
age = int(input('Enter age: '))

res = f"Hello {fullname}\nYou are {age} years old"

print(res)