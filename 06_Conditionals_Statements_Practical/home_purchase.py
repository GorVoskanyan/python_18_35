MIN_PRICE = 70000
MAX_PRICE = 100000

MAX_AREA = 100
MIN_AREA = 70

area = float(input('Area: '))

if MIN_AREA <= area <= MAX_AREA:
    price = float(input('Price: '))
    if MIN_PRICE <= price <= MAX_PRICE:
        print('Home is purchased...')
    else:
        print('Continue...')
else:
    print('Continue...')
