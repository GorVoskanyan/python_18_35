students_str = 'Hermine, Aram, Gor, Anahit'
students_list = ['Hermine', 'Aram', 'Gor', 'Anahit']

# print(len(students_list))
# print(len(students_str))
# print(type(students_list))

# indexing
first_char = students_str[0]
first_student = students_list[0]

# print(first_char)
# print(first_student)

# slicing
first_three_chars = students_str[0 : 3]
first_three_students = students_list[0 : 3]

# print(first_three_chars)
# print(first_three_students)

# mutable vs immutable
# print(id(students_str))
# students_str = students_str + 'END'
# print(id(students_str))
# print(students_str)

# print(id(students_list))
# students_list[0] = 'Nare'
# print(id(students_list))
# print(students_list)


# adding
students_list += ['Nare']
students_list.append('Arman')   # method
# students_list[0:0] = ['Hrayr']
students_list.insert(0, 'Hrayr')
# print(students_list)


# iterate over lists
# for student_name in students_list:
#     print(student_name)

# for index in range(len(students_list)):
#     print(index, students_list[index])

# for student_name in students_list:
#     print('Hello', student_name, '->', type(student_name))
#     for char in student_name:
#         print(char, end='++')
#     print()

# def add(a, b): return a + b
# l = [1, 1.1, True, 'text', [1, 2, 3], add]
# print(l)

# empty = []

# for number in range(10):
    # empty.append(number)
    # empty.insert(-1, number)
    # empty += [number]

# print(empty)



