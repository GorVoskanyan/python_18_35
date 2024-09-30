from functools import wraps
from typing import Callable, Any


def decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # Some code before wrapped function work
        result = func(*args, **kwargs)
        # Some code after function work
        return result
    return wrapper



