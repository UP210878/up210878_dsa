import math
import operator
import tkinter as tk

operators = ["+","-","*","/","^"] #Operadores
fnTrig = ["sen","sin", "cos", "tan",] 
afnTrig = ["cot", "sec", "csc","asin","atan","acos"]
fnLog = ["log","ln","aln","sin","alog","e"]
buttons=["1","2","3","4","5","6","7","8","9","+","-","*","/","^","sen","cos","tan","cot","sec","csc","(",")"]
#parenthesis_start = ['(','[','{',]
#parenthesis_finish = [')',']','}'] # Parentesis

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

root = tk.Tk()
root.geometry("1000x350")
root.title('CALCULATOR')
root.config(bg='#616161')

text_result = tk.Text(root, height=2, width= 60, font=("System",22))
text_result.grid(columnspan=60)
text_result.config(bg="#424242",fg="white")






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
    "e":math.exp,   
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
        except:
            clear_field()
            text_result.insert(1.0,"MathError")
            return
        i = i+1
    if len(Stack)>1: # Numeros separados sin signo se multiplican
        for i in range(0,len(Stack)-1):
            a = Stack.pop()
            b = Stack.pop()
            c = a * b
            Stack.append(c)
            
    return (Stack.pop())

# def Infix():
#     operacion = str(input("Ingrese la operacion con espacios entre cada numero/simbolo: "))
#     a = operacion.split()
#     return a

def Infix(input):
    operacion = str(input)
    a = operacion.split()
    return a


def Priority(Valor):
    if Valor in ["+","-"]:
        return 1
    elif Valor in ["*","/"]:
        return 2
    elif Valor in ["sen","cos","tan","sec","csc","cot","sin","ln","log","aln","alog","acos","asin","atan"]:
        return 4
    elif Valor in ["^"]:
        return 3
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

def makeCalculation(calculo):
        global calculation
        try:
            a = Infix(calculo)
            p = InfixtoPostfix(a)
            resultado = OperacionPostfix(p)
            calculation = ""
            text_result.delete(1.0,"end")
            text_result.insert(1.0,resultado)
        except:
            clear_field()
            text_result.insert(1.0,"MathError")

btn_1 = tk.Button(root,text="1",background="gray",fg="white",command=lambda: add_to_calculation(1),width=5, font=("Arial",14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root,text="2",background="gray",fg="white",command=lambda: add_to_calculation(2),width=5, font=("Arial",14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root,text="3",background="gray",fg="white",command=lambda: add_to_calculation(3),width=5, font=("Arial",14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root,text="4",background="gray",fg="white",command=lambda: add_to_calculation(4),width=5, font=("Arial",14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root,text="5",background="gray",fg="white",command=lambda: add_to_calculation(5),width=5, font=("Arial",14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root,text="6",background="gray",fg="white",command=lambda: add_to_calculation(6),width=5, font=("Arial",14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root,text="7",background="gray",fg="white",command=lambda: add_to_calculation(7),width=5, font=("Arial",14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root,text="8",background="gray",fg="white",command=lambda: add_to_calculation(8),width=5, font=("Arial",14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root,text="9",background="gray",fg="white",command=lambda: add_to_calculation(9),width=5, font=("Arial",14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root,text="0",background="gray",fg="white",command=lambda: add_to_calculation(0),width=5, font=("Arial",14))
btn_0.grid(row=5, column=2)

btn_period = tk.Button(root,text=".",background="gray",fg="white",command=lambda: add_to_calculation("."),width=5, font=("Arial",14))
btn_period.grid(row=5, column=1)

btn_sum = tk.Button(root,text="+",background="gray",fg="white",command=lambda: add_to_calculation(" + "),width=5, font=("Arial",14))
btn_sum.grid(row=2, column=5)

btn_minus = tk.Button(root,text="-",background="gray",fg="white",command=lambda: add_to_calculation(" - "),width=5, font=("Arial",14))
btn_minus.grid(row=3, column=5)

btn_mult = tk.Button(root,text="*",background="gray",fg="white",command=lambda: add_to_calculation(" * "),width=5, font=("Arial",14))
btn_mult.grid(row=4, column=5)

btn_div = tk.Button(root,text="/",background="gray",fg="white",command=lambda: add_to_calculation(" / "),width=5, font=("Arial",14))
btn_div.grid(row=5, column=5)

btn_div = tk.Button(root,text="^",background="gray",fg="white",command=lambda: add_to_calculation(" ^ "),width=5, font=("Arial",14))
btn_div.grid(row=6, column=5)

btn_open = tk.Button(root,text="(",background="gray",fg="white",command=lambda: add_to_calculation(" ( "),width=5, font=("Arial",14))
btn_open.grid(row=2, column=6)

btn_close = tk.Button(root,text=")",background="gray",fg="white",command=lambda: add_to_calculation(" ) "),width=5, font=("Arial",14))
btn_close.grid(row=3, column=6)

btn_neg = tk.Button(root,text="(-)",background="gray",fg="white",command=lambda: add_to_calculation(" -"),width=5, font=("Arial",14))
btn_neg.grid(row=4, column=6)

btn_log = tk.Button(root,text="log",background="gray",fg="white",command=lambda: add_to_calculation(" log "),width=5, font=("Arial",14))
btn_log.grid(row=5, column=6)

btn_ln = tk.Button(root,text="ln",background="gray",fg="white",command=lambda: add_to_calculation(" ln "),width=5, font=("Arial",14))
btn_ln.grid(row=6, column=6)

btn_alog = tk.Button(root,text="alog",background="gray",fg="white",command=lambda: add_to_calculation(" alog "),width=5, font=("Arial",14))
btn_alog.grid(row=5, column=7)

btn_aln = tk.Button(root,text="e",background="gray",fg="white",command=lambda: add_to_calculation(" e "),width=5, font=("Arial",14))
btn_aln.grid(row=6, column=7)

btn_sin = tk.Button(root,text="sin",background="gray",fg="white",command=lambda: add_to_calculation(" sin "),width=5, font=("Arial",14))
btn_sin.grid(row=6, column=1)

btn_cos = tk.Button(root,text="cos",background="gray",fg="white",command=lambda: add_to_calculation(" cos "),width=5, font=("Arial",14))
btn_cos.grid(row=6, column=2)

btn_tan = tk.Button(root,text="tan",background="gray",fg="white",command=lambda: add_to_calculation(" tan "),width=5, font=("Arial",14))
btn_tan.grid(row=6, column=3)

btn_asin = tk.Button(root,text=u'sin\u207b\u00b9',background="gray",fg="white",command=lambda: add_to_calculation(" asin "),width=5, font=("Arial",14))
btn_asin.grid(row=7, column=1)

btn_acos = tk.Button(root,text=u'cos\u207b\u00b9',background="gray",fg="white",command=lambda: add_to_calculation(" acos "),width=5, font=("Arial",14))
btn_acos.grid(row=7, column=2)

btn_atan = tk.Button(root,text=u'tan\u207b\u00b9',background="gray",fg="white",command=lambda: add_to_calculation(" atan "),width=5, font=("Arial",14))
btn_atan.grid(row=7, column=3)

btn_equals = tk.Button(root,text="=",background="gray",fg="white",command=lambda: makeCalculation(calculation),width=5, font=("Arial",14))
btn_equals.grid(row=5, column=3)

btn_reset = tk.Button(root,text="AC",background="gray",fg="white",command=clear_field,width=5,height=5, font=("Arial",14))
btn_reset.grid(row=1, column=7,rowspan=4)

root.mainloop()

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