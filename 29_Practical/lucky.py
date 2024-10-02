def lucky(n: int) -> bool:
    return sum(map(int, str(n)[:len(str(n)) // 2])) == sum(map(int, str(n)[len(str(n)) // 2:]))

print(lucky(12344321))