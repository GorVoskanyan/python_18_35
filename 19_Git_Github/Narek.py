# print("hello from Narek")

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a - 1)
    
num = int(input(">>>: "))
result = factorial(num)
print(result)