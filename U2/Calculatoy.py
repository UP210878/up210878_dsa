import math
import operator
# import tkinter as tk


# Make a calculator, buttons to display.
# 9 = Maneja parentesis, potencia, multiplicacion, division, suma, resta
# 10 = Funciones (log,ln, sen, cos, acos...)
#Infix = 5 * ( 6 + 2 ) - 12 / 4
#Posfix = 5 6 2 + * 12 4 / -
# = 6 2 + = 8
# = 5 8 * = 40
# = 12 4 / = 3
# = 40 3 - = 37
#Posfix agarra dos posiciones antes del operador (Ej. 6 2 +)
# Posfix a valor
# Centinala = finalizacion del problema
#Scan de todo
    # Si es operando(Numero), enviar a la pila
    # Si es operator (elif): B = quita de Stack, A+ pop from stack, C = A operador B. Push(C) al stack

#operacion = str(input("Ingrese la operacion"))

operators = ["+","-","*","/","^"] #Operadores
fnTrig = ["sen","sin", "cos", "tan",] 
afnTrig = ["cot", "sec", "csc","asin","atan","acos"]
fnLog = ["log","ln","aln","sin","alog"]
buttons=["1","2","3","4","5","6","7","8","9","+","-","*","/","^","sen","cos","tan","cot","sec","csc","(",")"]
#parenthesis_start = ['(','[','{',]
#parenthesis_finish = [')',']','}'] # Parentesis

calculation = ""








ops = {
    "+": operator.add,#Funcion suma
    "-": operator.sub,#Resta
    "*":operator.mul,#Multiplicacion
    "/":operator.truediv,#Division
    "^":operator.pow,#Potencia
    "sen":math.sin,
    "sin":math.sin,
    "cos":math.cos,
    "tan":math.tan,
    "cot":math.atan,
    "atan":math.atan,
    "sec":math.acos,
    "acos":math.acos,
    "csc":math.asin,
    "asin":math.asin,
    "log":math.log10,
    "ln":math.log,
    "aln":math.exp,  
}

def OperacionPostfix(P): # Operaciones posfix
    P = list(P)
    P.append(")")
    Stack = []
    i = 0
    while P[i]!=")":
        try:
            if P[i] in operators:
                B = Stack.pop()
                A = Stack.pop()
                C = ops[P[i]](A,B)
                Stack.append(C)
            elif P[i] in fnTrig:
                A = math.radians(Stack.pop())
                B = round(ops[P[i]](A),10)
                Stack.append(B)
            elif P[i] in afnTrig:
                A = (Stack.pop())
                B = round(ops[P[i]](A),10)
                B = round(math.degrees(B),10)
                Stack.append(B)
            elif P[i] in fnLog:
                if P[i] in ["alog"]:
                    A = Stack.pop()
                    B = math.pow(10,A)
                    Stack.append(B)
                else:
                    A = Stack.pop()
                    B = ops[P[i]](A)
                    Stack.append(B)
            elif P[i] not in operators:
                Stack.append(float(P[i]))
            else:
                print("Invalid output, exiting")
                break
        except ValueError:
            print ("MathError")
            return
        i = i+1
    if len(Stack)>1: # Numeros separados sin signo se multiplican
        for i in range(0,len(Stack)-1):
            a = Stack.pop()
            b = Stack.pop()
            c = a * b
            Stack.append(c)
            
    return (Stack.pop())

def Infix():
    operacion = str(input("Ingrese la operacion con espacios entre cada numero/simbolo: "))
    a = operacion.split()
    return a


def Priority(Valor):
    if Valor in ["+","-"]:
        return 1
    elif Valor in ["*","/"]:
        return 2
    elif Valor in ["sen","cos","tan","sec","csc","cot","sin","ln","log","aln","alog"]:
        return 3
    elif Valor in ["^"]:
        return 4
    elif Valor in ["("]:
        return 0
    else:
        return -1



def InfixtoPostfix(Infix):
    Infix = list(Infix)
    Infix.insert(0,"(")
    Infix.append(")")
    Postfix=[]
    Ops_Stack=[]
    for i in range(0,int(len(Infix))): 
        if Infix[i] in operators:# Operador
            for k in range(int(len(Ops_Stack))-1,-1,-1):#Saca del stack
                if Priority(Infix[i]) <= Priority(Ops_Stack[k]): 
                    A = Ops_Stack.pop()
                    Postfix.append(A)
                    continue
                else:
                    break
            Ops_Stack.append((Infix[i]))
        elif Infix[i] in fnLog:
            Ops_Stack.append((Infix[i]))
        elif Infix[i] in fnTrig or Infix[i] in afnTrig:
            Ops_Stack.append((Infix[i]))
        elif Infix[i] == "(": # (
            Ops_Stack.append((Infix[i]))
        elif Infix[i] == ")": # )
            for j in range(int(len(Ops_Stack))-1,-1,-1):
                if Ops_Stack[j]!="(":
                    A = Ops_Stack.pop()
                    Postfix.append(A)
                elif Ops_Stack[j]=="(":
                    Ops_Stack.pop()
                    break
        elif Infix[i] not in operators:
            Postfix.append(Infix[i])
    return Postfix

def Prio(lista):
    lista = list(lista)
    for i in range(0,int(len(lista))):
        if lista[i] in operators:
            print (lista[i], " = ", (math.ceil(int((operators.index(lista[i]))+1)/2)))
            # return operators.index(lista[i])
        else:
            print("",end="")

# Prioridad
# 1) + -
# 2) * /
# 3) ^
# 4) ( )


a = Infix()
print ("Infix: ", a)

p = InfixtoPostfix(a)
print ("Prioridad: ")
Prioridad = Prio(a)
print ("Posfix: ", p)

#P = ["5","6","2","+","*","12","4","/","-"]
print ("Prioridad: ")
Prioridad = Prio(p)

Resultado = OperacionPostfix(p)
print ("Resultado: ", Resultado)

# 1 / ( x + ( 1 / ( x + ( 1 / ( x + ( 1 / x ) ) ) ) ) )

#Prio
"""
+-
*/
Functions
^
()
"""