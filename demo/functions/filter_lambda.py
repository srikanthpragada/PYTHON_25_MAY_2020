names = ['Python', 'C#', 'C', 'Java']

nums = [10, 11, 15, 40, 50, 60]

for n in filter(lambda v: v % 2 == 0, nums):
    print(n)

for n in filter(lambda v: v % 2 != 0, nums):
    print(n)

for name in filter(lambda v: len(v) > 2, names):
    print(name)
