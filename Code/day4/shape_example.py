

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side *self.side


s1 = Shape()
s2 = Square(5)
s3 = "Triangle"
print(s1.area())
print(s2.area())
#print(s3.area())


if isinstance(s2, Shape):
    print(s2.area())

if isinstance(s3, Shape):
    print(s3.area())
