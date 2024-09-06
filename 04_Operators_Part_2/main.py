# Assignment operators

# a = 5
# # a = a + 2   # a += 2
# a += 2      # or a = a + 2
# a -= 4      # or a = a - 4
# a *= 3      # or a = a * 3
# a **= 2     # or a = a ** 2
# a /= 9      # or a = a / 9
# a //= 2     # or a = a // 2
# a %= 3      # or a = a % 3
# print(a)


# identity operators
# is, is not
# a = 5
# b = 7
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)


# membership operators
# in, not in

# word = 'python'
# letter = 'p'
# substring = 'tho'
# print(letter in word)
# print(substring in word)
# print(letter not in word)

# num = '1234'
# digit = '3'
# print(digit in num)


# logical operators
# and, or, not

# result = 2 > 3 and 6 > 2
# result = 4 > 3 or 1 > 2
# print(not result)

# result = (6 > 5 or 11 < 9) and 3 > 4
#        False  or  True
#       False  or     False
#             False
# print(result)

# word = 'python'
# length_object = len(word)
# print(length_object)

# username = input('Enter username: ')
# password = input('Enter password: ')
#
# if ('admin' in username or 'super' in username) and len(password) > 7:
#     print('Welcome!')
# else:
#     print('Try again!')


# bitwise operators
#       8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
#  25                   1   1   0   0   1
#  15                       1   1   1   1
#  &                    0   1   0   0   1
#  |                    1   1   1   1   1
#  ^                    1   0   1   1   0
#  ~ a   1   1   1   1  0   0   1   1   0
#  <<                1  1   1   1   0   0 | 0 0 0
#  >>                                   1 | 1   1   1  0 0 0
a = 25
b = 15
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~ a
left_shift = b << 2
right_shift = b >> 3

# b <<= 2
# b >>= 3
# print(b)
# print(right_shift)
# print(bin(15))
# print(int('11001', 2))
