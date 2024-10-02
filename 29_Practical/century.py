# class Century:
#     def __init__(self, year):
#         self.year = year
#
#     def convert(self):
#         return self.year // 100 if not self.year % 100 else self.year // 100 + 1


# century = Century(1901)
# print(century.convert())

# print(type(century))

# century = type('Century', (), {'convert': lambda year: year // 100 if not year % 100 else year // 100 + 1})
# print(century.convert(1900))
# print(type(century))