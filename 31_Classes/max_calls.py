from functools import wraps
from typing import Callable, Any


def max_call(MAX_CALLS):
    def decorator(func: Callable) -> Callable:
        CALLS = 0
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            nonlocal CALLS
            CALLS += 1
            if  CALLS > MAX_CALLS:
                raise Exception(f'Max calls: {MAX_CALLS}')

            res = func(*args, **kwargs)
            print('Call:', CALLS)
            return res
        return wrapper
    return decorator


@max_call(5)
def f(): pass

f()
f()
f()
f()
f()
f()
