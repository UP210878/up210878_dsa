from math import ceil
import operator

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

operators = ["+","-","*","/","^","^"] #Operadores
#parenthesis_start = ['(','[','{',]
#parenthesis_finish = [')',']','}'] # Parentesis

ops = {
    "+": operator.add,#Funcion suma
    "-": operator.sub,#Resta
    "*":operator.mul,#Multiplicacion
    "/":operator.truediv,#Division
    "^":operator.xor,#Potencia
}

def OperacionPostfix(P): # Operaciones posfix
    P = list(P)
    P.append(")")
    Stack = []
    i = 0
    while P[i]!=")":
        if P[i] not in operators:
            Stack.append(int(P[i]))
        elif P[i] in operators:
            B = Stack.pop()
            A = Stack.pop()
            C = ops[P[i]](A,B)
            Stack.append(C)
        else:
            print("Invalid output, exiting")
            break
        i = i+1
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
    elif Valor in ["^"]:
        return 3
    elif Valor in ["(",")"]:
        return -1



def InfixtoPostfix(Infix):
    Infix = list(Infix)
    Infix.insert(0,"(")
    Infix.append(")")
    Postfix=[]
    Ops_Stack=[]
    for i in range(0,int(len(Infix))): # Operador
        if Infix[i] in operators[0:5]:
            for k in range(int(len(Ops_Stack))-1,-1,-1):
                if Priority(Infix[i]) <= Priority(Ops_Stack[k]): 
                    A = Ops_Stack.pop()
                    Postfix.append(A)
                    break
                else:
                    break
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
            print (lista[i], " = ", (ceil(int((operators.index(lista[i]))+1)/2)))
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

P = InfixtoPostfix(a)
print ("Prioridad: ")
Prioridad = Prio(a)
print ("Posfix: ", P)

#P = ["5","6","2","+","*","12","4","/","-"]
print ("Prioridad: ")
Prioridad = Prio(P)

Resultado = OperacionPostfix(P)
print ("Resultado: ", Resultado)
