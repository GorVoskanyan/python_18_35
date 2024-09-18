class Water:
    x = 1

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()

    def __gt__(self, other):
         if isinstance(other, Water):
             return self.x > other.x

    def __truediv__(self, other):
        ...

    def __sub__(self, other):
        ...

    def __mul__(self, other):
        ...

class Steam():
    ...

class Storm():
    ...

class Air:
    ...

class Earth:
    ...

class Fire:
    ...


water = Water()
water2 = Water()
water2.x = 10
water.x = 30
air = Air()

storm = water + air
print(water > water2)