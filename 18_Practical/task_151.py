import sys

if len(sys.argv) < 2:
    print('Not a command line arguments')

try:
    for filename in sys.argv[1:]:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())
        print('-'*25)
except FileNotFoundError:
    print('Unknown file.')