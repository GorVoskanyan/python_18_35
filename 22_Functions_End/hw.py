def unpack(collection: list) -> list:
    if not collection:
        return []

    if isinstance(collection[0], list):
        return unpack(collection[0])
    else:
        return [collection[0]] + unpack(collection[1:])


# l = [1, 1, [1, [1, [1, 1, 1, [1, 1, [1]]]]]]
# res = unpack(l)
# print(res)


def _sum():
    n = int(input('>>> '))
    return 0 if not n else n + _sum()

# _sum = _sum()
# print(_sum)


def int_to_binary(n: int) -> str:
    if not n: return ''
    return int_to_binary(n // 2) + str(n % 2)

# binary = int_to_binary(7)
# print(binary)
# print(bin(7))

def is_palindrome(word):
    if len(word) < 1:
        return True

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    return False

word = input("Enter your word here : -> ")
res = is_palindrome(word)
print(res)