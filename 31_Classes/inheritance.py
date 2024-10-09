class Main: pass


class A(Main): pass


class B(Main): pass


class C(Main): pass


class D(Main): pass


class X(A, B): pass


class Y(B, C): pass


class Z(C, D): pass


class M1(X, Y): pass


class M2(Y, Z): pass


# print(M2.mro())     # method resolution order
# print(M2.__mro__)


class Figure:
    def __init__(self, pos_x, pos_y, size1, size2):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size1 = size1
        self.size2 = size2

    def change_position(self, new_pos_x, new_pos_y):
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y


class ResizebleMixin:
    def resize(self, new_size1, new_size2):
        self.size1 = new_size1
        self.size2 = new_size2


class Rectangle(Figure, ResizebleMixin):
    pass


class Square(Figure, ResizebleMixin):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)


rectangle1 = Rectangle(1, 1, 3, 4)
rectangle2 = Rectangle(2, 2, 5, 6)
square = Square(3, 3, 3)

for figure in [rectangle1, rectangle2, square]:
    new_size2 = figure.size2 * 2
    new_size1 = figure.size1 * 2
    figure.resize(new_size1, new_size2)

# print(rectangle2.size1)
print(square.size1)
print(square.size2)