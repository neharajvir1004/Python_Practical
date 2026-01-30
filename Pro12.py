#Use of Local, Global and Nonlocal Variable. 

x = 10   

def outer():
    y = 20   

    def inner():
        z = 30   
        print("Local z =", z)

    inner()
    print("Nonlocal y =", y)

outer()
print("Global x =", x)
