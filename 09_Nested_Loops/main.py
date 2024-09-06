# Nested loops
# Template
# for row in range(size):
#   for col in range(size):
#        ...

# 1 1 2 3 4 5
# 2 3 4 5 6 7
# 3 4 5 6 7 8
# 4 5 6 7 8 9
# 5 6 7 8 9 10

# for row in range(6):
#     for col in range(6):
#         print(row + col, end='\t')
#     print()


# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row * col, end='\t')
#     print()


# next prime number
# n = int(input("Enter number: "))
# while True:
#     n += 1
#     for divider in range(2, n):
#         if n % divider == 0:
#             break
#     else:
#         print(n, 'is next prime number')
#         break


# palindrome words
# def check_is_palindrome(collection):
#     for word in collection:
#         print(word, end=':\t')
#         while word != '':
#             if word[0] != word[-1]: # indexing
#                 print('is not palindrome')
#                 break
#             word = word[1:-1]   # sliceing
#         else:
#             print('is palindrome')
#
# words = 'madam', 'engine', 'level', 'python'
# check_is_palindrome(words)


# 1 0 0 0 0
# 2 1 0 0 0
# 2 2 1 0 0
# 2 2 2 1 0
# 2 2 2 2 1

# def draw_matrix(size):
#     for row in range(size):
#         for col in range(size):
#             if row == col:
#                 print(1, end='  ')
#             elif row < col:
#                 print(0, end='  ')
#             else:
#                 print(2, end='  ')
#         print()

# size = int(input('Enter size of matrix: '))
# draw_matrix(size)


#        |
#        |
#------------------
#        |
#        |

# def draw_coordinate_plane(height, width):
#     for row in range(height):
#         for col in range(width):
#             if col == width // 2:
#                 print('|', end='')
#             elif row == height // 2:
#                 print('-', end='')
#             else:
#                 print(' ', end='')
#         print()
#
# height = int(input('Enter height: '))
# width = int(input('Enter width: '))
#
# draw_coordinate_plane(height=height, width=width)



