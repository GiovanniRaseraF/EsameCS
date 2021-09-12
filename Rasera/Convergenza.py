fx = input("F(x)= ")

while(True):
    m = eval(input("m= "))
    x0 = eval(input("x0= "))

    x = x0
    for i in range(0,1000):
        x = x - (eval(fx)/m)

    print(str(x))