import time
import functools
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f'Function works: {runtime:.8f} seconds')
        return result
    return wrapped_func

@timer
def square_sum():
    """ Calculate sum of 1-1000 squares. """
    return sum((i ** 2 for i in range(10000)))

@timer
def cubes_sum(number):
    return sum((i ** 3 for i in range(number + 1)))


# my_square_sum = square_sum()
# print(my_square_sum)
# print()
# my_cubes_sum = cubes_sum(10000)
# print(my_cubes_sum)


print(square_sum.__doc__)
print(square_sum.__name__)