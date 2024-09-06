#HOMWORk


#HOMEWORK. 1

# 0       2       4       6       8       10
# 1       3       5       7       9       11
# 2       4       6       8       10      12
# 3       5       7       9       11      13
# 4       6       8       10      12      14
# 5       7       9       11      13      15


# n = 0,2,4,6,8,10

# for col in range(6):
#         for row in (n):
#             print(row + col, end='\t')
#         print()

#HOMWORk.2

# |-----------------------------|
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |-----------------------------|


# def painting (height , width):
#     for row in range(height):
#         for col in range(width):
#             if row == 0 or row == height - 1:
#                 if col == 0 or col == width - 1:
#                     print('|', end='')
#                 else:
#                     print('-', end='')
#             else:
#                 if col == 0 or col == width - 1:
#                     print('|', end='')
#                 else:
#                     print(' ', end='')    
#         print()        

# height = int(input('Enter height: '))
# width = int(input('Enter width: '))

# painting(height=height, width=width)

#HOMWORK3

#             1
#          3    5
#       7     9    11
#    13    15    17   19
# 21    23    25    27    29


# def Triangle():
#     starting_number = 1

#     row = 1
#     while row <= n :
#         print(' ' * (n - row) * 3, end='')
     
#         for i in range(row) :
#             print(starting_number, end='    ')
#             starting_number += 2
#         print()
#         row += 1    

# n = int(input('enter a number of rows: '))

# Triangle()

#ahavor erkar em mtacel :( u haziv exela :)


#HOMWORK4

# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345


# n = int(input('enter a number: '))
#
# for row in range(1, n+1):
#     for i in range(n,n - row,-1):
#         print(i, end='')
#     for j in range((n - row) * 2):
#         print('.', end='')
#     for i in range(n - row + 1, n + 1):
#         print(i, end='')
#     print()



#ORVA KESY GNAC SRA VRA    :(