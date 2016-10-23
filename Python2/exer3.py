DIGIT = input("Enter 10 digit number:")
DIGIT = [int(i) for i in DIGIT]
ODD = []
EVEN = []
if (len(DIGIT)!= 10):
    print("invalid number")
else:
    for i in range (0,10):
        if (DIGIT[i]%2 == 0):
            ODD.append(DIGIT[i])
        else:
            EVEN.append(DIGIT[i])
    for i in range (0,len(EVEN)):
        print(EVEN[i], end=' ')
    print('\n')
    for i in range (0,len(ODD)):
        print('',ODD[i],end='')
        
