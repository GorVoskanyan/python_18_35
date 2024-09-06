# List methods

# class im_list(list):
#     def patahakan_jnjel(self):
#         self.pop(__import__('random').randint(0, len(self) - 1))
#
# im_list = im_list()
# im_list.append(1)
# im_list.append(2)
# im_list.append(3)
# im_list.append(4)
# im_list.patahakan_jnjel()
# print(im_list)



students = ['Hermine', 'Nare', 'Anahit']

# add
students.append('Aram')
students.insert(0, 'Arman')

new_students = ['Hrayr', 'Gor']
# new_students = 'Hrayr, Gor'
# students.append(new_students)
students.extend(new_students)

# remove
students.remove('Nare')

last = students.pop()
first = students.pop(0)
# students.pop(50)

# students.clear()

# print(students)
# print(last)
# print(first)


# count, index
students.append('Aram')
aram_count = students.count('Aram')
# print(aram_count)

# aram_index = students.index('Gor')
# aram_index = students.index('Aram', 3)
# aram_index = students.index('Aram', 3, 17)
# print(aram_index)


# sort, reverse
# students.reverse()

# students.append('aram')
# students.sort()
# students.sort(reverse=True)
# students.sort(key=str.lower)

# def my_lower(elem): return elem.lower()
# students.sort(key=my_lower)

# students.sort(key=lambda elem: elem.lower())
# students.sort(key=lambda elem: elem.lower(), reverse=True)

# copy
# students_copy = students
students.append(['Arman', 'Gor'])
# students_copy = students.copy()
# students_copy = students[:]
# print(id(students))
# print(id(students_copy))
# students_copy.remove('aram')

import copy

students_copy = copy.deepcopy(students)
students[-1][-1] = 'Hrayr'

# print(students_copy)
# print(students)

# del students[0]
del students

# print(students)