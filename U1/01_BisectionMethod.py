
'''
Date: 15/01/2023 
Author: Vinc3nt
Email: UP210878@alumnos.upa.edu.mx
Description: Bisection method for obtaining a root, exported into python from C++. 
Based on this code: https://github.com/carlosherrerah/Matricula_DSA/blob/05bb35a8a344c80fe0c16140df2e0a4081263928/Biseccion.cpp
Last Modification: 15/01/2023
'''

#------------ PREPROCESSOR DIRECTIVES ----------------

import math #Logaritmos

#----------------------------------------------------

def Equation(value): #Equation for solving
    return (value**2) - 2

x1 = 1. #Starting point
x2 = 2. #Finish point
xmedia = None # Wouldbe Root
Error_Absoluto = 0.001 # Absolute error
Error_Relativo = abs(x2-x1) # Relative error
i = 1 #Counter for repetitions
it = round((math.log(x2 - x1) - math.log(Error_Absoluto)) / math.log(2)) #Iterations, how many times will the program repeat
print ("Ecuacion actual: x^2 - 2")
print ("Iteraciones:",it)

print("i","x1","x2","Er","xm","f(x1)","f(xm)","f(x1) * f(xm)\n",sep="\t\t|")
while Error_Relativo >= Error_Absoluto:
    xmedia = (x1+x2) / 2
    print (i, round (x1,4), round(x2,4), round(Error_Relativo,4), round(xmedia,4),  round(Equation(x1),4), round(Equation(xmedia),4), round(Equation(x1)*Equation(x2),4),"\n",sep= "\t\t")
    if Equation(x1) * Equation(xmedia) < 0:
        x2 = xmedia;
    else:
        x1=xmedia;
    Error_Relativo = abs(x2 - x1);
    i = i+1

print ("La raiz es aproximadamente ", xmedia)

