from functools import wraps
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        nonlocal count
        res = func(*args, **kwargs)
        # wrapper.count += 1
        count += 1
        print(count)
        # print(wrapper.count)
        return res
    # wrapper.count = 0

    return wrapper

@counter
def test(): print('ok')

test()
test()
test()
