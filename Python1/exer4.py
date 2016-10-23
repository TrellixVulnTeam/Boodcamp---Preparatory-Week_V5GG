import math
a_temp = input("Enter the value of a:")
b_temp = input("Enter the value of b:")
c_temp = input("Enter the value of c:")
a = int(a_temp)
b = int(b_temp)
c = int(c_temp)
if (b**2 - 4*a*c) < 0 :
    print("No real-valued solutions exists")
else :
    x = (-b+ math.sqrt(b**2 - 4*a*c))/(2*a)
    y = a*(x**2) + b*x + c
    print("The output is", y)
