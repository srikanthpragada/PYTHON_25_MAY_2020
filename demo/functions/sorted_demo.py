nums = [-10, 10, -5, 60, -80]

names = ['Abc','Xy','Pqrs','Defgh','Bc']

for n in sorted(nums, key=abs):
    print(n)

for n in sorted(names, key = len):
    print(n)

