string = input("Enter binary sequence:")
counter0=0
counter1=0
counter0max=0
counter1max=0
for i in range (0,len(string)):
    if (string[i] == "0"):
        counter0 = counter0 + 1
        counter1 = 0
    elif (string[i] == "1"):
        counter1 = counter1 + 1
        counter0 = 0
    else:
        print("Not a binary sequence.")
        break
    if (counter0 > counter0max):
        counter0max = counter0
    if (counter1 > counter1max):
        counter1max = counter1
if (counter0max > counter1max):
    print("Longest run was zeros with length:", counter0max)
elif (counter1max > counter0max):
    print("Longest run was ones with length:", counter1max)
else:
    print("Equal run of ones and zeros with length:", counter1max)
