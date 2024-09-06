# for loops

# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1

# for number in 2, 7, 63, 89:
#     print(number ** 2)

# -----------
# winners = 0
# tickets = 234, 83251, 132513, 513, 31241, 314, 3124
#
# for ticket in tickets:
#     if ticket % 2 == 0:
#         print('Lucky ticket!')
#         winners += 1    # keep counter
#
# print(winners, 'winners')


# range(start, stop, step) function
# for i in range(10, 21, 2):
#     print(i ** 2)

# begin = int(input('Enter start: '))
# end = int(input('Enter end: '))
#
# for number in range(begin, end, -2):
#     print(number ** 2)


# prime numbers

# number = int(input('>>> '))
#
# for divider in range(2, number):
#     if number % divider == 0:
#         print(number, 'has divider', divider)
#         break
# else:
#     print(number, 'is prime')


# text = 'Python'
#
# for i in range(5):
#     print(text, i)

# *
# **
# ***
# ****
# *****

# symbol = '*'

# for i in range(1, 6):
#     print(symbol * i)

# for i in range(5, 0, -1):
#     print(symbol * i)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{(i * j):4d}", end='')
#     print()

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print("%4d"%(i * j), end='')
#         j += 1
#     i += 1
#     print()
