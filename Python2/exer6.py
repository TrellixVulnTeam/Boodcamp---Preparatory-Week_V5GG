DIGIT = input("Enter numbers:")
for i in range (0,len(DIGIT),9):
    print(' ',DIGIT[i],end='|')
print('\n')
for i in range (2,len(DIGIT),9):
    print('',DIGIT[i:(i+2)],end='|')
print('\n')
for i in range (5,len(DIGIT),9):
    print(DIGIT[i:(i+3)],end='|')
