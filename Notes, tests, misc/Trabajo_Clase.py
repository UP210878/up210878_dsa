c0 = int(input("Dame un numero"))
i = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0/2
    else:
        c0 = 3*c0+1
    i += 1
    print (c0)
print (i)


for digit in "34030490":
    if digit == "0":
        print("X", end="")
        continue
    print(digit,end="")