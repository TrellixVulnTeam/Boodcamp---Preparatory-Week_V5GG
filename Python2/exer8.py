temp = input("Enter number sequence:")
t1=[]
t2=[]
SUM=0
for i in range (0,len(temp),2):
    t1.append(temp[i])
for i in range (1,len(temp),2):
    t2.append(temp[i])
tt1=''.join(t1)
tt2=''.join(t2)
if (len(tt1)==len(tt2)):
    for i in range (0,len(tt1)):
        SUM = SUM + int(tt1[i])*int(tt2[i])
else:
    for i in range (0,len(tt1)-1):
        SUM = SUM + int(tt1[i])*int(tt2[i])
    SUM = SUM + int(tt1[len(tt1)-1])
print(SUM)
