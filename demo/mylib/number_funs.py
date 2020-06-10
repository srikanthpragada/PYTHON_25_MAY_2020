# Number related functions

import math


def iseven(n):
    """
    Returns true if given number(n) is even otherwise false
    """
    return n % 2 == 0


def isprime(n):
    """
       Returns true if given number(n) is prime number, otherwise false
    """

    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    print(iseven(11), isprime(25))
else:
    print('Importing ', __name__)
