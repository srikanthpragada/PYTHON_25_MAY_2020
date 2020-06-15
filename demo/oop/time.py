class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    @property
    def hours(self):
        return self.h

    @hours.setter
    def hours(self, value):
        if value >= 0 and value <= 23:
            self.h = value
        else:
            raise ValueError("Invalid hours")


t = Time(10, 20, 30)
t.hours = 15
print(t.hours)

t2 = t
t2.hours = 20
print(t.hours)




