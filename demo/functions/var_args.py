def fun(*names):  # Varying argument
    print(type(names))


fun("java", "python", "c")
fun("A", "B")
fun("A", "B", 'C', "D")
