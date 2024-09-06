# Conditional statements

# n = int(input('>>> '))

# if n % 2 == 0:
#     print(n, 'is even')
# else:
#     print(n, 'is odd')

# nested conditions
# if n > 0:
#     print(n, 'is positive')
#     if n % 2 == 0:
#         print(n, 'is even')
#     else:
#         print(n, 'is odd')
# elif n == 0:
#     print(n, 'is zero')
# else:
#     print(n, 'is negative')


# ternary operator
# result = 'negative' if n < 0 else 'positive'
# print(result)


# is_rain = int(input('1 or 0: '))
#
# if is_rain:
#     print('Rain')
# else:
#     print('Not')


# calculator
main_menu = """1. Arithmetic
2. Geometric"""

choice = input(main_menu + '\nSelect: ')

if choice == '1':
    num_1 = float(input('>>> '))
    operator = input('[+/-/*///] Select: ')
    num_2 = float(input('>>> '))

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 + num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == '/':
        print(num_1 / num_2)
    else:
        print('unknown operator')
elif choice == '2':
    pass
