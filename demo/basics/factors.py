# Program to take a number and display all factors

num = int(input("Enter a number :"))

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n)
