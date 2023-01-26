a = [45,32,65,43,41]
print (a)
for i in range(0,len(a)):
    a[-1-i]=a[i]
    a[i]=a[-1-i]
print (a)