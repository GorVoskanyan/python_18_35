# unpacking
x, y = input('Enter coordinates: ')
y = int(y)

if (x in 'aceg' and y % 2 == 0) \
        or (x not in 'aceg' and y % 2 != 0):
        print('White')
else:
    print('Black')
