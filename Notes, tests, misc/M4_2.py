def isPar(x):#Funcion
    if x%2 == 0:
        return True
    else:
        return False

print (isPar(23))

y = (lambda x: x + 3)(6) ## 6+3
print (y)

lista = [4,7,1]
ordenada = sorted(lista)
print (ordenada)

y = list(map(lambda x:x+3,lista))
print(y)

mayores = list(filter(lambda x: x>3,lista))#Dame a manera de lista, un filtro usando lambda de la lista
print ("Mayores", mayores)

## OPERADOR TERNARIO
#codigo si de culmpe [if] [condicion] [else] [si no]

a = 10
b = 2
c = a/b if b!=0 else -1
print (c)