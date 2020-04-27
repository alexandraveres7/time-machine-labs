class Rectangle:
    def _calculate(self):
        return self.sides[0] * self.sides[1]

    @property
    def area(self):
        if not hasattr(self, '_area'):
            self._area = self._calculate()
        return self._area


class Square(Rectangle):
    def __init__(self, side):
        self.sides = [side, side]


r = Rectangle()
r.sides = [4, 3]
print(r._calculate())
s = Square(10)
print(s.area)
