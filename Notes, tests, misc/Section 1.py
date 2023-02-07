#Section 1
print ("Hello", "World", end="...", sep=" ") #end = final de linea, sep = separacion de cada impresion(por default es espacio)
print ("\n\n")
print ("Hello", "World", end="\n", sep="____")
print ('WOrld '*2)
#funciones se manejan por posicion, nombre o combinado. Para manejar combinado primero se necesita poner los de posicion (ej. 
#"Hola") antes de los nombres (ej. "end, sep")
'''
COMENTARIOS A FORMA DE BLOQUE
'''
print ('Greg\'s Book')#\' Hace que se imprima la comilla y no se confunda el print 
print ("Greg\'s Book")

a = "Ave"
b = "Maria"
c = a + b#Concatenar

print (c)
print("   *   ","  * *  "," *   * ","*     *","*** ***","  * *  ","  * *  ","  ***  ", sep="\n")

import array as arr
a = arr.array('i', [1,2,3])# el 'i' simboliza el tipo de dato en el array
print(a)#Imprime todo el array
print(a[1])#Imprime un elemento del array en la posicion
b = [55,22,"33"]
print (b[2])
b.append("44")#Agregar valor a array
print (b)
b.pop(1)#Quitar un elemento, si no pones nada, quita el ultimo
print(b)