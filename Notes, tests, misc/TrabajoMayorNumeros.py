#a,b,c. Mayor de los 3 METODO 1 

a = int (input("Dame el valor de a: "))
b = int (input("Dame el valor de b: "))
c = int (input("Dame el valor de c: "))

# Metodo max
'''
print("El valor maximo es ",max(a,b,c))
'''
# Metodo lista
'''
valores = [a,b,c]
valores.sort(reverse=True)
print("El mayor valor es ",valores[0])
'''
# Metodo if
'''
max = None
if a > b and a > c:
    max = a

elif b > a and b > c:
    max = b

elif c > a and c > b:
    max = c

print ("El mayor numero es", mayor)
    
'''
# Sin variables, operadores basicos, for, max (Puro If)

if a > b:
    if a > c:
        print (a)
    elif c > a:
        print (c)
elif b > a:
    if b > c:
        print (b)
    elif c > b:
        print (c)
