temp1 = input("Enter dates:")
y=0
dd1=[]
mm1=[]
yy1=[]
dd2=[]
mm2=[]
yy2=[]

for i in range(0,len(temp1)):
    y=y+1
    if (temp1[i]!='/'):
        dd1.append(temp1[i])
    else:
        break
for i in range(y,len(temp1)):
    y=y+1
    if (temp1[i]!='/'):
        mm1.append(temp1[i])
    else:
        break
for i in range(y,len(temp1)):
    y=y+1
    if (temp1[i]!=' '):
        yy1.append(temp1[i])
    else:
        break
for i in range(y,len(temp1)):
    y=y+1
    if (temp1[i]!='/'):
        dd2.append(temp1[i])
    else:
        break
for i in range(y,len(temp1)):
    y=y+1
    if (temp1[i]!='/'):
        mm2.append(temp1[i])
    else:
        break
for i in range(y,len(temp1)):
    y=y+1
    if (temp1[i]!='/'):
        yy2.append(temp1[i])
    else:
        break

d1=''.join(dd1)
d1=int(d1)
d2=''.join(dd2)
d2=int(d2)
m1=''.join(mm1)
m1=int(m1)
m2=''.join(mm2)
m2=int(m2)
y1=''.join(yy1)
y1=int(y1)
y2=''.join(yy2)
y2=int(y2)

c1 = (365*y1)+(y1//4)-(y1//100)+(y1//400)+((306*m1+5)//10)+(d1-1)
c2 = (365*y2)+(y2//4)-(y2//100)+(y2//400)+((306*m2+5)//10)+(d2-1)

if (c1>c2):
    count=c1-c2
else:
    count=c2-c1
print(count, "days.")


    
        
    
