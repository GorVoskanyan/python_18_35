import datetime
from functools import wraps
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            print(f"{func.__name__} run...")
            res = func(*args, **kwargs)
            print(f"{func.__name__} end...")
            return res
        except Exception as msg:
            with open('errors.log', 'a', encoding='utf-8') as log_file:
                log_file.write(f"'{func.__name__}' - [{datetime.datetime.now()}] - [{msg}]\n")

    return wrapper

@logging
def test(a, b):
    return a / b

print(test(1, 0))
