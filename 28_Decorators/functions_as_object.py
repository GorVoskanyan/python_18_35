import time

def timer(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    runtime = end - start
    print(f'Function works: {runtime:.8f} seconds')
    return result


def square_sum():
    return sum((i ** 2 for i in range(10000)))

def cubes_sum(number):
    return sum((i ** 3 for i in range(number + 1)))


my_square_sum = timer(square_sum)
print(my_square_sum)
print()
my_cubes_sum = timer(cubes_sum, 10000)
print(my_cubes_sum)