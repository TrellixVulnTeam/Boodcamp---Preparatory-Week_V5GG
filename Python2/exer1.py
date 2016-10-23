TIN = input("Enter Tax Identification Number:")
TIN = [int(i) for i in TIN]
if (len(TIN) != 9):
    print("Invalid number")
else:
    check = TIN[8]
    SUM = 0
    for i in range(1,9):
        SUM = SUM + TIN[i-1]*(2**(9-i))
    temp = SUM%11
    temp1 = temp%10
    if (temp1 == check):
        print("Tax Identification Number Valid.")
    else:
        print("Tax Identification Number not Valid.")
