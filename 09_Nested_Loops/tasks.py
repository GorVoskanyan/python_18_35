#Smartcode_tasks_1

size = int(input(">>>"))

for row in range(size):
    for col in range(size):
        print(row + col, end="\t")
    print()

#Smartcode_tasks_2


# def rectangle(height,width):
#     for row in range(height):
#         for col in range(width):
#             if row == height - 1 or row == 0 :
#                 print("-",end="")
#             elif col == width - 1 or col == 0 :
#                 print("/",end="")
            
#             else:
#                 if col == 0 or col == width - 1:
#                     print("/",end="")
#                 else:
#                     print(" ",end="")
#         print()

# heigth = int(input("Enter heigth..."))
# width = int(input("Enter width..."))
# rectangle(height=heigth,width=width)

#Smartcode_tasks_3

# def triangle():
#     num = 1
    
#     row = 1
#     while row <= n:
#         print(" " * (n - row) * 3,end="")
        
#         for i in range(row):
#             print(num,end="   ")
#             num += 2
#         print()
#         row += 1


# n = 5

# triangle()

#Smartcode_tasks_4

# def rectangle():