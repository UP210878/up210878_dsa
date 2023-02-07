import operator
# Make a calculator, buttons to display.
# 9 = Maneja parentesis, potencia, multiplicacion, division, suma, resta
# 10 = Funciones (log,ln, sen, cos, acos...)
#Infix = 5*(6+2)-12/4
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

operators = ["+","-","/","^","*"] #Operadores
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
    print (Stack.pop())

P = ["5","6","2","+","*","12","4","/","-"]
OperacionPostfix(P)