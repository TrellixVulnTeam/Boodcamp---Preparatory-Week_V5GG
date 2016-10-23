import math
side1_t = input("Give the size of the first side of the triange")
side2_t = input("Give the size of the second side of the triange")
side3_t = input("Give the size of the third side of the triange")
a = float(side1_t)
b = float(side2_t)
c = float(side3_t)
area = (1/4)*math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))
print(area)
