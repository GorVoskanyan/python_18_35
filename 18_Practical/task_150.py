import sys

if len(sys.argv) < 2:
    sys.exit('Arguments must be provided command line.')

try:
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        print(''.join(file.readlines()[-10:]))
except FileNotFoundError as e:
    print('File not found.', e)
