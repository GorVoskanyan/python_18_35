# import string
# # indexing, alphabet
#
# # alphabet = 'abcdefgh...'
# alphabet = string.ascii_lowercase * 2
#
# code = ''
# text = input('Enter text: ')
# shift = int(input('Enter shift: '))
#
# for char in text:
#     # print(index, text[index])
#     code += alphabet[alphabet.index(char) + shift]
#
# print(code)


import main

main.draw_triangle()