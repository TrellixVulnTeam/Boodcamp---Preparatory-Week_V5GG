DIGIT = input("Enter 8-bit binary numner :")
DIGIT = [int(i) for i in DIGIT]
if (len(DIGIT)!= 8):
    print("Invalid number")
else:
    CHECK = DIGIT[7]
    t=0
    for i in range (0,6):
        if (DIGIT[i] == 1):
            t=t+1
    if (CHECK == t%2):
        print("Parity check OK.")
    else:
        print("Parity check NOT OK.")
