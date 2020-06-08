g = 100  # global variable

def fun1():
    global g
    a = 10  # Enclosing variable
    g = 200

    def fun2():  # Local function
        b = 20
        print(a)

    fun2()
    print(a,g)

fun1()
print(g)
