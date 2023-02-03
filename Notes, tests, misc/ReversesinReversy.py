a = [45,32,65,43,41,3,24,5,4,3,5]
print (a)
for i in range(0, (int(len(a)/2))):
    a[i],a[-i-1] = a[-i-1],a[i]
print (a)