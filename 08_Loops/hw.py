import random

pc_number = random.randint(1, 100)
user_number = int(input('>>> '))

while pc_number != user_number:
    if pc_number > user_number:
        print('Try greater number')
    else:
        print('Try lesser number')
    user_number = int(input('>>> '))
print('You guess number!')