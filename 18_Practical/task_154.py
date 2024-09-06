import sys

filename = sys.argv[1]
# data = dict()
try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

        # for letter in text:
        #     if letter.isalpha():
        #         if letter in data:
        #             data[letter] += 1
        #         else:
        #             data[letter] = 1

        data = {letter: text.count(letter) for letter in text if letter.isalpha()}
    print(data)
except FileNotFoundError:
    print('unknown file.')