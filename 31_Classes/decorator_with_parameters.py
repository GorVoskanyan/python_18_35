from functools import wraps
import time

def decorator_with_parameter(precision):
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            runtime = round(time.time() - start, precision)
            print(runtime)
            return result
        return wrapper
    return timer


@decorator_with_parameter(2)
def f(): return sum(i**3 for i in range(100000))

r = f()
print(r)