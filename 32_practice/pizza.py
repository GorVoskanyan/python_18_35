"""
Մուտքագրեք պատվերների քանակը։ 6
Պատվեր 1։ Գոռ Պեպերոնի 1
Պատվեր 2։ Արամ Նրբություն 2
Պատվեր 3։ Գոռ Պեպերոնի 2
Պատվեր 4։ Գոռ Հռոմեական 3
Պատվեր 5։ Արամ Հռոմեական 5
Պատվեր 6։ Գոռ Իտալական 4

Պատվերներ։
Գոռ։
Իտալական 4
Հռոմեական 3
Պեպերոնի 3

Արամ։
Հռոմեական 5
Նրբություն 2
"""

database = dict()

orders_count = int(input('Մուտքագրեք պատվերների քանակը։ '))
for i in range(1, orders_count + 1):
    username, pizza_name, pizza_quantity = input(f'Պատվեր {i}։ ').split()
    pizza_quantity = int(pizza_quantity)
    if username not in database:
        database[username] = {pizza_name: pizza_quantity}
    elif pizza_name in database[username]:
        database[username][pizza_name] += pizza_quantity
    else:
        database[username][pizza_name] = pizza_quantity

print()
print('Պատվերներ։')
for username in database:
    print(f"{username}:")
    for pizza_name, pizza_quantity in sorted(database[username].items()):
        print(f"{pizza_name} {pizza_quantity}")
    print()
