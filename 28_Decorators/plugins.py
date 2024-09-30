from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()

def register(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello, {name}"


@register
def say_goodbye(name):
    return f"Goodbye, {name}"


print(PLUGINS)
print(say_hello('Milena'))
print(say_goodbye('Milena'))