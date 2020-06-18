l = [1, 2, 3]

try:
    l.add(4)
    print("Done")
except ValueError:
    print("Value Error")
except Exception as ex:
    print("Error :", ex)
else:
    print("Success")

print("Over")
