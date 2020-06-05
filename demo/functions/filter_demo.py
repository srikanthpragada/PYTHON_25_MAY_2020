names = ['Python','C#','C','Java']

# takes a value and returns boolean
def iseven(n):
    return n % 2 == 0

def bigname(n):
    return len(n) > 2


nums = [10, 11, 15, 40, 50, 60]

for n in filter(iseven, nums):
    print(n)

for c in filter(str.isupper, "Hello LI"):
     print(c)

for name in filter(bigname, names):
     print(name)






