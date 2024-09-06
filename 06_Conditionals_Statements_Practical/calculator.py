import math

print(' ' * 20 + 'Welcome to our Calculator')

main_menu = "1. Area\n2. Volume\n"

choice = input(main_menu + 'Select: ')

if choice == '1':
    sub_menu = "1. Rectangle\n2. Triangle\n3. Cyrcle\n"
    choice = input(sub_menu + 'Select: ')
    if choice == '1':
        length = float(input('Enter length: '))
        width = float(input('Enter width: '))
        area = length * width
    elif choice == '2':
        a = float(input('Enter side: '))
        h = float(input('Enter height: '))
        area = a * h / 2
    elif choice == '3':
        r = float(input('Enter radius: '))
        area = math.pi * r ** 2

    print(area, 'm^2')
elif choice == '2':
    pass    # Todo
