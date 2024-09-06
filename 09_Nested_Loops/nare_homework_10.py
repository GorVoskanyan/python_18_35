# 0       2       4       6       8       10
# 1       3       5       7       9       11
# 2       4       6       8       10      12
# 3       5       7       9       11      13
# 4       6       8       10      12      14
# 5       7       9       11      13      15

n = 0,2,4,6,8,10
for col in range(6):
       for row in (n):
           print(col + row, end='\t')
       print()




#h.w N2.
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

#def draw_square(height, width):
#     for row in range(height):
#         for col in range(width):
#            if row == 0 or row == height - 1:
#                if col == 0 or col == width - 1:
#                   print("|", end='')
#                else:
#                    print('-', end='')
#             else:
#                 if col == 0 or col == width - 1:
#                    print("|", end='')
#                 else:
#                    print(' ', end='')
#         print()

#height = int(input('Enter height: '))
#width = int(input('Enter width: '))

#draw_square(height=height, width=width)









