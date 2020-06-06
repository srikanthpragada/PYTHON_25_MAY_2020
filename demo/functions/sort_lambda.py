names = ['Python', 'C#', 'C', 'Java']

nums = [10, 11, 15, 40, 50, 60]

for n in sorted(names, key=lambda v: v[0]):
    print(n)
