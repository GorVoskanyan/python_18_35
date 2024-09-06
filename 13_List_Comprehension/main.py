# List comprehension

# nums = []
# for num in range(10):
#     if num % 2 == 0:
#         nums.append(num)
#     else:
#         nums.append(num ** 3)

# nums = [num if num % 2 == 0 else num ** 3 for num in range(10)]
# print(nums)


# l = [2 * char for char in 'python']
# print(l)

# nums = list(range(10))
# print(nums)
# chars = list('python')
# print(chars)


# import time
#
# start = time.time()
# nums = []
# for i in range(100):
#     for j in range(100):
#         for k in range(100):
#             if i ** 2 + j ** 2 == k ** 2:
#                 nums.append([i, j, k])
# runtime = time.time() - start
#
# print(runtime)

# s = time.time()
# n = [[i, j, k] for i in range(100) for j in range(100) for k in range(100) if i ** 2 + j ** 2 == k ** 2]
# r = time.time() - s
# print(r)


# Nested lists
# students = [['Hermine', 10], ['Nare', 20], ['Anahit', 30]]

# for student_info in students:
#     print(student_info)
#     for s_n in student_info:
#         print(s_n, end='==>')
#     print()
# print(students[0][0])
# print(students[0][1])


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix)

# unpacked = [subelem for elem in matrix for subelem in elem]

# for elem in matrix:
#     # print(elem)
#     for subelem in elem:
#         # print(subelem)
#         unpacked.append(subelem)

# print(unpacked)


