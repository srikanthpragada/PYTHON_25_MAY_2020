def process(n):
    print("Processing ", n)


print(id(process))


def process(n1, n2):
    print("Processing ", n1, n2)


print(id(process))
# process(10)
