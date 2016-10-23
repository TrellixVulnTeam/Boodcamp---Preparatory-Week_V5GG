y = input("Enter year:")
y = int(y)
if (y>2099 or y<1900):
    print("Invalid year.")
else:
    a = y%4
    b = y%7
    c = y%19
    d = (19*c+15)%30
    e = (2*a+4*b-d+34)%7
    month = (d+e+114)//31
    day = ((d+e+114)%31)+14
    if (day>30):
        day = day - 30
        month = month + 1
    print("Day:",day)
    print("Month:",month)
