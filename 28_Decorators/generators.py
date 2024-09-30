def fibonacci(number: int):
    cur_val, next_val = 0, 1

    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
    return


fibo_10 = fibonacci(10)
print(fibo_10)

for fib in fibo_10:
    print(fib)


# generators
my_gen = (i**2 for i in range(10))
print(my_gen)

for elem in my_gen:
    print(elem)


