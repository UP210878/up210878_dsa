
'''
Date: 15/01/2023 
Author: Vinc3nt
Email: UP210878@alumnos.upa.edu.mx
Description: Bisection method for obtaining a root, exported into python from C++.
Last Modification: 15/01/2023
'''

#------------ PREPROCESSOR DIRECTIVES ----------------

import math 

#----------------------------------------------------

def Equation(value):
    return (value**2) - 2

x1 = 1
x2 = 2
xm = None
Es = 0.001
Er = abs(x2-x1)
i = 1
it = round((math.log(x2 - x1) - math.log(Es)) / math.log(2))
print (it)

print("i   |     x1    |     x2    |      Er   |     xm    |" \
           "   f(x1)   |   f(xm)   | f(x1) * f(xm) |\n")
while Er >= Es:
    xm = (x1+x2) / 2
    print (i, x1, x2, Er, xm,  Equation(x1), Equation(xm), Equation(x1)*Equation(x2),"\n",sep= "\t")
    if ((x1**2) - 2) * ((xm**2) - 2) < 0:
        x2 = xm;
    else:
        x1=xm;
    Er = abs(x2 - x1);
    i = i+1

print (xm)

