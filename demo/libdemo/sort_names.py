f = open("names.txt", "rt")  # Write text

names = []
for name in f.readlines():
    names.append(name)

f.close()

for name in sorted(names):
    print(name.strip())

