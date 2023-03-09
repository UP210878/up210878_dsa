# Vicente Valenzuela Martinez
# UP210878
# 8 / 03 / 23

def moveToRight(LIST,ITERATIONS): # Move [LIST] to the right [ITERATIONS] times
    LIST = list(LIST)
    for i in range(0,ITERATIONS):
        A = LIST.pop()
        LIST.insert(0,A)
    return LIST

def isBalanced(LIST): # Check if parenthesis in [LIST] close correctly
    LIST = list(LIST)
    Stack = []
    for i in range(0,len(LIST)):
        if LIST[i] == "(":
            Stack.append(LIST[i])
        elif LIST[i] == ")":
            if len(Stack) == 0:
                return False
            else:
                Stack.pop()
    if len(Stack) > 0:
        return False
    else: return True


lista = [1,2,3,4,5,6,7,8,9]
print(lista)
times = int(input('How many times would you like to move the contents to the right: '))
lista = moveToRight(lista,times)
print (lista)

print ('\n========================================================================================\n')

vector = ["(())()","(()",")()(","(a*+())b()","("]
for i in range(0,len(vector)):
    Resultado = isBalanced(vector[i])
    print (vector[i], "=", Resultado)


