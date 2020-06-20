# Generator
def numbers():
    for i in range(1, 11):
        yield i


g = numbers()
print(type(g))
print(next(g))
print(next(g))


# for v in g:
#     print(v, end = ' ')


