class Student:
    # Constructor
    def __init__(self, name, course="Python"):
        # object attributes
        self.name = name
        self.course = course
        self.feepaid = 0

    def get_total_fee(self):
        if self.course == 'Python':
            return 5000
        else:
            return 4000

    def payment(self, amount):
        if self.feepaid + amount > self.get_total_fee():
            raise ValueError("Feepaid is more than total fee to be paid!")
        else:
            self.feepaid += amount

    def get_due(self):
        return self.get_total_fee() - self.feepaid


s1 = Student("Steve")
print(s1.name, s1.course)
print(s1.get_total_fee())
s2 = Student("Roberts", 'Java')
s2.payment(3000)
s2.payment(2000)
print(s2.get_due())
