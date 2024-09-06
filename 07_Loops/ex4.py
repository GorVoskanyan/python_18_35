# MIN_price = 70000
# MAX_price = 100000

# MIN_area = 70
# MAX_area = 100

# area = float(input('Area: '))

# if MIN_area <= area <= MAX_area: 
#     price = float(input('Price: '))
#     if MIN_price <= price <= MAX_price:
#         print('Home is purchased!')
#     else: 
#         print('Continue...')
# else:
#     print('Continue...') 


 
# #Lessons WHILE LOOPS!

# pin = input('Enter pin:')

# if pin == '12345':
#     print('Wlecome...')
# else: 
#     print('Try again!')



# pin = input('Enter pin:')

# while pin != '1235':
#     print('Try again!')
#     pin = input('Enter pin: ')



# pin = input('Enter pin: ')

# while pin != '12345':
#     print('Try again!')
#     pin = input('Enter pin: ')

# print('Welcome!')



# while True:
#     pin = input('Enter pin: ')
#     if pin == '12345':
#        break
#     print('Try again!')



# PIN = '12345'
# while True:
#     pin = input('Enter pin: ')
#     if pin == PIN:
#        print('Welcome')
#        break 
#     print('Try again!')



# i = 1
# while True:
#     if i <= 10:
#         print(i)
#         i += 1
#     else:
#         break



# i = 1
# while i <= 10: 
#     i += 3
#     print(i)
#     if i % 2 == 0:
#         continue
#     print(i)



# num = input('Enter number or "q" for quit: ')
# summ = 0

# while num != 'q':
#     num = float(num)
#     summ += num 
#     num = input('enter number or "q" for quit: ')


# print('Summ: ', summ)
    

# num = input('Enter number or "q" for quit: ')
# summ = 0
# input_count = 0

# while num != 'q':
#      num = float(num)
#      summ += num 
#      input_count += 1
#      num = input('Enter number or "q" for quit: ')

# print('Summ: ', summ)
# print('Inputs: ',  input_count)


# Calculator_1

# while True:
#     length = input('Enter legth or "q" for quit: ')
#     if length == 'q':
#         break
#     length = float(length)
#     width = float(input('Enter width or "q" for quit:'))
#     area = length * width 
#     print(area, 'm^2')


#Calculator_2 

# while True:
#     length = input('Enter legth or "q" for quit: ')
#     width = input('Enter width or "q" for quit:')
    
#     if length == 'q' or width == 'q':
#         break
#     length = float(length)
#     width = float(width)
#     area = length * width
# print(area, 'm^2')


# 1 - 1 
# 2 - 4 
# 3 - 9 
# ...

# i = 1
# while i <= 10:
#     print(i, '-', i**2, '-', i**3)
#     i += 1



# 100 - 1000
# 98 - 9604 
# ...

# i = 100
# while i >= 90:
#     if i % 2 == 0:
#       print(i, '-', i ** 2 )
#     i -= 1



# num = 12463466

# while num: 
#     print(num % 10, end = '')
#     num //= 10



# num = int(input('>>>  '))

# while num:

#     print(num % 10, end= ' ')
#     num //= 10


# while num := int(input('>>>  ')):
#     print(num ** 2)