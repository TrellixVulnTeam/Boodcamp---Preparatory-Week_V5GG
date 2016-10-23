DIGIT = input("Enter 9 digit number:")
DIGIT = [int(i) for i in DIGIT]
if (len(DIGIT)!= 9):
    print("invalid number")
else:
    for i in range (0,len(DIGIT),3):
        print(DIGIT[i],end='  ')
    print('\n')
    for i in range (1,len(DIGIT),3):
        print('',DIGIT[i],end=' ')
    print('\n')
    for i in range (2,len(DIGIT),3):
        print(' ',DIGIT[i],end='')
