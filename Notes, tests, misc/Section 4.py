# Section 4 U2

""" comments
import mypkg.sibling # Cargar parte de la libreria
from mypkg import sibling # Forma alternativa

sb.sort(a) #Del paquete sb, usa la funcion sb
"""

# hash
# PEP8 - Style guide for python # fechaNacimiento [Camello] #fecha_nacimiento [Snake]
# variables - containers - boxes
# PYthon is sensitive:
_n = 1
n = 2
N = 3
_1 =10
exchange_rate = None

# Python is dynamically-typed language, changes value-type based on value, no need to declare
m = 5
print(m)
m = "Hello"
print(m)

keywords = ['False','None','True','and','continue','def','del','elif','else','except','from','global','if','import','in','is','lambda0','not','or','pass','forward']



print(keywords[1], keywords.index('True')) #Imprime la palabra en la posicion 2 (Contando desde 0), imprime la posicion de la palabra 'True'
print(keywords.pop(), keywords.pop(), keywords.pop(1), keywords[1]) #.pop quita
keywords.append('Hola') #Poner al final
keywords.insert(2,'Dale') #Poner en cierto punto en la lista
print(keywords[2])
print(keywords[-1])
print(keywords.count('False'))
#Shortcut operands

x = 2
x += 3
print(x)
print(round(3.234234,4)) #Redondear a X numero de digitos

y = "5" + "2" #concatenar
print(y)


print (len(keywords)) # Elementos de una lista