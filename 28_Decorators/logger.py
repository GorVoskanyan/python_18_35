import time
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f'Function works: {runtime:.8f} seconds')
        return result
    return wrapped_func

def logging(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(
            f"Function: {func.__name__} start work\t"
            f"Positional arguments: {args}\t"
            f"Keyword arguments: {kwargs}"
        )
        result = func(*args, **kwargs)
        print(f"Function successfully ended")
        return result
    return wrapper


@logging
@timer
def square_sum():
    return sum((i ** 2 for i in range(10000)))


@timer
@logging
def cubes_sum(number):
    return sum((i ** 3 for i in range(number + 1)))


my_square_sum = square_sum()
print(my_square_sum)
print()
my_cubes_sum = cubes_sum(10000)
print(my_cubes_sum)