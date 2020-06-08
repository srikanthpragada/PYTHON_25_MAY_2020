
def set_zero(n):
    print(id(n))
    n = 0


a = 100
print(id(a))
set_zero(a)
print(a)
