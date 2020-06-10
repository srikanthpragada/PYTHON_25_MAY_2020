import sys

if len(sys.argv) < 2:
    print("Usage : python table.py <number> [length]")
    exit(1)

if len(sys.argv) == 2:
    length = 10  # Default length
else:
    length = int(sys.argv[2])

num = int(sys.argv[1])  # Number for which table is to be displayed

for i in range(1, length + 1):
    print(f"{num:3} * {i:2} = {num * i:5}")
