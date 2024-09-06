# print function sep, end
# text = 'Python!\n'
# print(text * 5, end='')

# print('Hello', end='|||')
# print('World!', end='\n')

# print('Hello', 'World', sep='__')


# Arithmetic operators
# print(8 + 5)
# print(8 - 5)

# print(8 * 2)
# print(8 ** 3)

# print(8 / 5)
# print(8 // 5)
# print(8 % 5)    # modulo

# statement = (5 + 7) * (2 ** (3 / 4))
# print(statement)


# -------
# amount = int(input('Enter amount: '))
# coin_1 = 500
# coin_2 = 200
# coin_3 = 100
#
# coin_1_quantity = amount // coin_1
# amount = amount % coin_1    # or amount %= coin_1
# coin_2_quantity = amount // coin_2
# amount = amount % coin_2    # or amount %= coin_2
# coin_3_quantity = amount // coin_3
# amount %= coin_3    # or amount = amount % coin_3
#
# print(coin_1, '-', coin_1_quantity)
# print(coin_2, coin_2_quantity, sep=' - ')
# print(coin_3, coin_3_quantity, sep=' - ')


# ------
# num = 1234
# n1 = num // 1000
# n2 = num // 100 % 10
# n3 = num % 100 // 10
# n4 = num % 10

# print(n4, n3, n2, n1, sep='')


# check the number is even or odd
# num = int(input('>>> '))
# if num % 2 == 0:
#     print(num, 'is even')
# else:
#     print(num, 'is odd')


# comparison operators
greater = 5 > 5 # -> boolean type
greater_or_equal = 8 >= 5

less = 5 < 8
less_or_equal = 5 <= 8

is_equal = 5 == 8
not_equal = 5 != 6
# print(not_equal)

# a = int(input('>>> '))
# b = int(input('>>> '))
#
# maximum = (a + b + abs(a - b)) // 2
# print(maximum)