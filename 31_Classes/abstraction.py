from abc import ABC, abstractmethod, abstractproperty, abstractstaticmethod, abstractclassmethod


class Shape(ABC):

    # @property
    # @abstractproperty
    # @abstractstaticmethod
    # @abstractclassmethod
    @abstractmethod
    def x(self):
        return 1

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, side, heigth) -> None:
        self.side = side
        self.heigth = heigth

    def area(self):
        return (self.side * self.heigth) / 2


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


rect = Rectangle(3, 4)