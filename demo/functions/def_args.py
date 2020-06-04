def wish(name, message):
    print(message, name)


def table(num=15, len=5):
    for n in range(1, len + 1):
        print(f"{num:3} * {n:2} = {num * n:5}")


# table()
# table(20)
# table(23, 3)
table(len=7)  # keyword argument
table(len=7, num=11)  # keyword arguments
wish(message="Hello", name = 'Bob')  # Keyword parameters
wish("David","Good Evening")  # positional parameters
