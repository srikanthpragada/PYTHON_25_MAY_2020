class Student:
    # Constructor
    def __init__(self, name, course="Python"):
        # object attributes
        self.name = name
        self.course = course

    def get_total_fee(self):
        if self.course == 'Python':
            return 5000
        else:
            return 4000


s1 = Student("Steve")
print(s1.name, s1.course)
print(s1.get_total_fee())

s2 = Student("Roberts",'Java')

