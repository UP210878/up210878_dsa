
#LISTAS

#numpy libreria de numeros

numbers = [100,343,42,32]
print (sorted(numbers))


for i in range (0, len(numbers)):
    print(numbers[i], end="\t")
print ("\n")
for i in numbers:
    print(i, end = "\t")
print()

numbers[0] = 111
print(numbers)

numbers.remove(32)## REmover el elemnto por caracter
del numbers[1]## REmover por posicion
#append al final
#insert, le dices posicion
# pop, borrar el ultimo valor
# del numbers[-1]. lo mismo que pop pero no muestra que valor quito

lista = []
sumatoria = 0
for i in range(10):
    lista.append((i+1)*2)
    sumatoria += lista[i]
print (lista)
print (sumatoria)
# print (np.sum(lista)) ## numpy sumatoria

#variable.split == divide una cadena en vector
#lambda == funcion que no existe
