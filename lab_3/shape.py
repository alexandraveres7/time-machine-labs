class Shape:
    def __init__(self):
        self.name = 'shape'

    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2


s = Square(36)
print(s.name)
print(s.area())

