print('Ողջույն ես հաշվիչ եմ!')

choice = input('Ընտրեք՝\n1․ Ուղղանկյուն\n2․ Եռանկյուն\n3. Շրջանագիծ\n>>> ')

if choice == '1':
    length = input('Մուտքագրեք երկարությունը։ ')
    length = float(length)
    # print(type(length))

    width = input('Մուտքագրեք լայնությունը։ ')
    width = float(width)

    # area of rectangle length * width
    area = length * width
    # area = int(area)
    print(area, 'm^2')
elif choice == '2':
    a = input('Մոտքագրեք առաջին կողմը։ ')
    a = float(a)
    b = float(input('Մուտքագրեք երկրորդ կողմը։ '))
    c = float(input('Մուտքագրեք երրորդ կողմը։ '))

    # formula Herona s = (P * (P - a) * (p - b) * (p - c)) ** 0.5

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s, 'm^2')
elif choice == '3':
    radius = float(input('Մուտքագրեք շառավիղը։ '))
    area = 3.14 * (radius ** 2)
    print(area, 'm^2')
else:
    print('Խնդրում ենք մուտքագրել 1, 2 կամ 3')