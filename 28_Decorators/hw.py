class PrimeNumbers:
    def __init__(self, count):
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count:
            self.start += 1
            if self._is_prime(self.start):
                self.count -= 1
                return self.start
        raise StopIteration


    def _is_prime(self, number: int) -> bool:
        for div in range(2, int(number ** 0.5) + 1):
            if number % div == 0:
                return False
        return True


primes = PrimeNumbers(10)
# print(primes.__next__())
# print(primes.__next__())

for prime in primes: print(prime, end='|')
for prime in primes: print(prime, end='|')