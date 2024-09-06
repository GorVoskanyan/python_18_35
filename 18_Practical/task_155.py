import sys

filename = sys.argv[1]
try:
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().lower().split()
        data = dict()
        for word in words:
            if not word[-1].isalpha():
                word = word[:-1]
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
    print(data)
except FileNotFoundError:
    print('unknown file.')