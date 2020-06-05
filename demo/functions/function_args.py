def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def operation(a, b, process):
    return process(a, b)


print(operation(10, 20, add))
print(operation(10, 20, mul))
