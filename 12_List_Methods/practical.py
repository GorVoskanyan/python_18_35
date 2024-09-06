"""
"Մուտքում ունեք 6 ամբողջ թվեր։
Ձեր խնդիրն է դրանցից ստեղծել նոր ցուցակ, որտեղ յուրաքանչյուր տարր կլինի`
երկու թվերի գումարը՝ տվյալ թվի և իրեն հաջորդող թվի գումարը:"
"""

# numbers_string = input('Մուտքագրեք թվերը իրարից անջատված բացատներով։ ').split()
# numbers_list = list(map(int, input('Մուտքագրեք թվերը իրարից անջատված բացատներով։ ').split()))
# numbers_list = numbers_string.split(' ')
# numbers_list = []

# list comprehension
# numbers_list = [int(num) for num in numbers_string]

# for str_num in numbers_string:
#     numbers_list.append(int(str_num))

# print(numbers_string)
# print(numbers_list)

# new_list = [numbers_list[i] + numbers_list[i + 1] for i in range(len(numbers_list) - 1)]

# for index in range(len(numbers_list) - 1):
#     _sum = numbers_list[index] + numbers_list[index + 1]
#     new_list.append(_sum)

# print(new_list)

# a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
# numbers_list = [a, b, c, d, e, f]
# new_list = []
# for i in range(len(numbers_list) - 1):
#     new_list.append(numbers_list[i] + numbers_list[i + 1])
#
# print(new_list)



# ex2
# first = 'apple'
# second = 'orange'
# third = 'blueberry'
# fourth = 'banana'
# fifth = 'kiwi'

# first_list = list(first + second + third + fourth + fifth)
# print(first_list)

# new_list = []
# new_list.extend(first)
# new_list.extend(second)
# new_list.extend(third)
# new_list.extend(fourth)
# new_list.extend(fifth)
# print(new_list)

