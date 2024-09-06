def function(collection, target):
    return [
        [collection[i], collection[j]]
        for i in range(len(collection))
        for j in range(len(collection))
        if collection[i] + collection[j] == target
    ]

# res = function(collection=[1, 2, 4, 7, 11], target=9)
# print(res)


from random import randint

n = int(input('>>> '))
l = list(range(1, n + 1))
print(l)
num = randint(1, n)

before_sum = sum(l)
l.remove(num)
print(l)
after_sum = sum(l)
print(before_sum - after_sum)
