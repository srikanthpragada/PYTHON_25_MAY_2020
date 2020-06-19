class InvalidTimeError(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message is None:
            return "Invalid Time"
        else:
            return self.message


class Time:
    def __init__(self, h, m, s):
        if h >= 0 and h <= 23:
            self.h = h
        else:
            raise InvalidTimeError(f"Invalid Hour : {h}")

        if m >= 0 and m <= 59:
            self.m = m
        else:
            raise InvalidTimeError(f"Invalid Minute : {m}")

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
            raise InvalidTimeError(f"Invalid Hour : {value}")


t = Time(10, 80, 30)
