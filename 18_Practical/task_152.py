try:
    input_file = input('Enter input file: ')
    with open(input_file, 'r', encoding='utf-8') as file:
        data = [f"{i}. {line}" for i, line in enumerate(file.readlines(), 1)]
    output_file = input('Enter output file: ')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(data)
except FileNotFoundError:
    print('unknown file')

