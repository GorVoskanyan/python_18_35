import sys

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    words = file.read().split()

max_length = len(max(words, key=len))
max_length_words = [word for word in words if len(word) == max_length]

print('Max length:', max_length)
print('Max length words:', max_length_words)