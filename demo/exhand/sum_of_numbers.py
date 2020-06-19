total = 0

while True:
    try:
        num = int(input("Enter number : "))
        if num == 0:
            break

        total += num
    except:
        print("Invalid Number!")

print("Total = ", total)
