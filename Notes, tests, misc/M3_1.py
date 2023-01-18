'''
a = 2
b = 4
if a > b:
    print ("Hola")
elif b > a:
    print ("Hola2")

# Una tupla no se incrementa, es estatico, un arreglo si.
#  (1,2,3) TUPLA
#  [1,2,3...] ARREGLO/LISTA
c = (2,3,4)
print(type(c))
d = [3,6,4]
print(type(d))
'''

# ------------------------------------- EJERCICIO -------------------------------------

'''
Averiguar si un ano es bisiesto o no. Si el ano no es divisible entre 4, es un anio comun. Si el anio no es divisible por 100, es un ano bisiesto
o si no, si el numero no es divisible entre 400, es un ano comun, si no, es un ano bisiesto.

Tip, usa != y %.
'''
'''
ano = int (input("Dame el ano "))
if ano < 1582:
    print("No gregoriano")
elif ano % 4 != 0:
    print("Common year")
elif ano % 100 != 0:
    print ("Leap year")
elif ano % 400 != 0:
    print ("Common year")
else:
    print ("Leap year")

# Las asignaciones se hacen en paralelo, no en serie.
# No do while.

'''
'''
a = 1
i = 1
while a > 0:
    i = i+1
    print(i)
'''

even_numbers = 0
odd_numbers = 0
number = int(input("Enter a number"))
while number != 0:
    number = int(input("Enter a number"))
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
print ("Odd numbers:", odd_numbers)
print ("Even numbers:", even_numbers)

counter = 3
while counter: #Sin condicionantes, mientras el numero sea diferente de 0, TRUE, igual a 0, FALSE
    print (counter)
    counter -= 1
print ("outside the loop")