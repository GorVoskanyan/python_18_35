class RandomNumber:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__limit > self.__counter:
            self.__counter += 1
            return __import__('random').randint(1, 10)
        else:
            raise StopIteration


obj = RandomNumber(limit=3)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

for random_number in obj:
    print(random_number)