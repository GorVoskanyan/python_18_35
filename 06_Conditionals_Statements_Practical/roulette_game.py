import random

lucky_number = random.randint(-1, 36)

if lucky_number == -1:
    print('Выпавший номер: 00…')
    print('Выигравшая ставка: 00')
elif lucky_number == 0:
    print('Выпавший номер: 0…')
    print('Выигравшая ставка: 0')
else:
    reds = '1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34, 36'
    print('Выпавший номер:', lucky_number)
    print('Выигравшая ставка:', lucky_number)
    print('Выигравшая ставка:', 'красное' if str(lucky_number) in reds else 'черное')
    print('Выигравшая ставка:',  'нечетное' if lucky_number % 2 != 0 else 'четное')
    print('Выигравшая ставка:', 'от 1 до 18' if lucky_number in range(1, 19) else 'от 19 до 36')
