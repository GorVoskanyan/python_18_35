# # Functions
#
# # define function
# # def main():
# #     choice = input('1.Draw rectangle\n2.Draw Triangle\nSelect: ')
# #
# #     if choice == '1':
#           # call function
# #         draw_rectangle()
# #     elif choice == '2':
# #         draw_triangle()
# #     else:
# #         print('Unknown')
# #
# #
# # def draw_rectangle():
# #     size = 5
# #     for row in range(size):
# #         print('#' * size)
# #
# # def draw_triangle():
# #     size = 5
# #     n = 1
# #     for line in range(size):
# #         print(' ' * (size - line - 1), end='')
# #         print('# ' * (n))
# #         n += 1
#
# # main()
#
#
# # return statement
# # def is_equal(x, y):
# #     return x == y
#
# # print(is_equal(3, 3))
#
# # x = int(input('Enter x: '))
# # y = int(input('Enter y: '))
# # if is_equal(x, y):
# #     print('is equal')
# # else:
# #     print('not equal')
#
#
# # def is_palindrome(word):
# #     while word:
# #         if word[0] != word[-1]:
# #             return False
# #         word = word[1:-1]
# #
# #     return True
#
#
# # if is_palindrome('madam'):
# #     print('madam is palindrome')
# # else:
# #     print('madam is not palindrome')
#
#
# def password_generator() -> str:
#     from string import ascii_lowercase
#     from random import choice
#     alphabet = ascii_lowercase
#     password = ''
#     for _ in range(8):
#         # password += __import__('random').choice(alphabet)
#         password += choice(alphabet)
#     return password
#
# # password = password_generator()
# # print('Random password is:', password)
#
#
# def check_password(password: str) -> bool:
#     if len(password) < 8:
#         return False
#
#     lower = upper = digit = 0
#
#     for char in password:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1
#         elif char.isdigit():
#             digit += 1
#
#     if lower and upper and digit:
#         return True
#     return False
#
# password = password_generator()
#
# if check_password('a@31Aafdas'):
#     print('Password is strong!')
# else:
#     print('Please change password!')


def pifagor(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


# def main():
#     a = float(input('Enter a: '))
#     b = float(input('Enter b: '))
#     c = pifagor(a, b)
#     print('c =', c)

# main()


def taxometer(distance):
    distance *= 1000    # metr
    BASE = 4
    total = BASE + (distance / 140) * 0.25
    return total


def main():
    distance = float(input('Enter distance in km: '))
    cost = taxometer(distance)
    # cost = round(cost)
    # print(cost, '$')
    print(f'{cost:.2f} $')

main()