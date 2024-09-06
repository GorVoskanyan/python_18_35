file = open('../18_Practical/text.txt', 'w', encoding='utf-8')
# file = open('text.txt', 'a', encoding='utf-8')
# file = open('text.txt', 'r', encoding='utf-8')

# print(type(file))
# file.write('Բարև\nԱշխարհ\n!\n')
file.writelines([f"{i} - {i ** 2}\n" for i in range(1, 10)])

# one_string = file.read()
# one_string = file.read(5)
# print(one_string)
# print(len(one_string))

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline(3))

# all_lines_list = file.readlines()
# print(all_lines_list)

# for char in file.read():
#     print(char)
#
# for line in file:
#     print(line)

# file.close()
# print(file)



# context manager
# with open('text.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line.rstrip())
#
# print('File is closed')


