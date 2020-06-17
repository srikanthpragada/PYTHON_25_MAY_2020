class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x * self.y > other.x * other.y

    def __add__(self, other):
        return Point(self.x + other, self.y + other)


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"{super().__str__()},{self.radius}"


c1 = Circle(10, 20, 50)
c2 = Circle(10, 30, 100)
print(c1)  # c.__str__()
print(c1 == c2)


# p1 = Point(10, 20)
# p2 = Point(10, 20)
# p3 = Point(5, 5)
# # print(id(p1), id(p2))
# print(p1 == p2)  # p1.__eq__(p2)
# print(p1)  # str(p1) -->   p1.__str__()
# print(p1 > p3)
#
# p2 = p1 + 10
# print(p2)
