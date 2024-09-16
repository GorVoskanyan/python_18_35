# *arguments **keyword arguments

# def function(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# function(1, 2, a=1, b=2)


# positional and keyword arguments
# def function(pos_only, /, kwd_or_pos, *, kwd_only):
#     print(pos_only)
#     print(kwd_or_pos)
#     print(kwd_only)

# function('poitional', kwd_or_pos='positional or keyword', kwd_only='keyword only')


# default values
# def function(*args, seperator=' '):
#     print(seperator.join(args))

# function('a', 'b', 'c')


# lambda functions
# add = lambda a, b: a + b
# print(add(3, 4))

# def f(a):
#     return lambda b: a + b

# _sum = f(1)(2)
# print(_sum)

# l = [(4, 1), (2, 3), (-1, -2)]
# l.sort(key=lambda t: t[-1])
# print(l)


# map, filter, reduce
# numbers = ['1', '2', '3']
# int_numbers = list(map(int, numbers))
# int_numbers = [int(number) for number in numbers]
# print(int_numbers)


# numbers = [-1, 2, -3, 4]
# filtered_numbers = list(filter(lambda x: x > 0, numbers))
# filtered_numbers = list(map(lambda x: x > 0, numbers))
# print(filtered_numbers)



from functools import reduce
# numbers = [-1, 2, -3, 4]
# _sum = reduce(lambda x, y: x + y, numbers)
# print(_sum)


from functools import cache
import sys

sys.setrecursionlimit(5000)
@cache
def fibo(n): return n if n < 2 else fibo(n-1) + fibo(n-2)

res = fibo(1000)
print(res)