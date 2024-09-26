# # EX6 converter
#
#
# class Converter:
#     def __init__(self, length, unit):
#         self.length = length
#         self.unit = unit
#
#     def to_meters(self):
#         if self.unit == "meters":
#           return self.length
#         elif self.unit == "inches":
#             return self.length * 0.0254
#         elif self.unit == "feet":
#             return self.length * 0.3048
#         elif self.unit == "yard":
#             return self.length * 0.9144
#         elif self.unit == "miles":
#             return self.length * 1609.34
#         elif self.unit == "kilometers":
#             return self.length * 1000
#         elif self.unit == "centimeters":
#             return self.length * 0.01
#         elif self.unit == "millimeters":
#             return self.length * 0.001
#         else:
#             raise ValueError("Unsupported value: ")
#
# length_converter = Converter(14, "miles")
# length_in_meters = length_converter.to_meters()
# print(length_in_meters)
#
