class Person:
    def __init__(self, name, age):
        # Object attributes
        self.__name = name  # private attribute
        self.__age = age

    def get_type(self):
        if self.__age < 20:
            return "Young"
        elif self.__age <= 50:
            return "Middle-aged"
        else:
            return "Old"


p = Person("Bill", 60)
p._Person__age = 50  # Private attribute is accessed from outside
print(p.__dict__)
print(p.get_type())
