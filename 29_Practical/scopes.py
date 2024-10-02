# LEGB local, enclosed, global, built-in

# x = 'global'
# def f1():
#     global x
#     x = 'enclosed'
#     def f2():
#         # nonlocal x
#         x = 'local'
#         print(x)
#     f2()
#     print(x)
#
# f1()
# print(x)
