# parametros viven dentro de la funcion
# argumentos los envias desde fuera a una funcion

def saludo(name):
    print("Welcome to python", name)

def potencia(base, exponente = 2):##VAlor default de 2 del exponente, pero se puede cambiar
    return base**exponente

name = input("Nombre: ")
saludo(name)

y= potencia(2,3)
z = potencia (exponente=3,base=2)
x = potencia(2)
print (y,x,z)

####Funcion cuatratica (a=1, c=15, b=-8)

def cuadratica(a=1,b=-8,c=15):
    return (-b+((b**2)-(4*a*c))*.5)/(2*a)

y = cuadratica()
print ("Cuadratica: ", y)

####################################
