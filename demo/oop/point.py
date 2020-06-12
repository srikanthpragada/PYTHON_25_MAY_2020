
class Point:
    def __init__(self,x = 0 ,y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"


p1 = Point(10,20)
p2 = Point(10,20)
print(id(p1),id(p2))
print(p1 == p2)
print(p1) #  str(p1) -->   p1.__str__()

