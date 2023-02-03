
lista1 =[]
elementos_lista = int(input("Ingrese cuantos valores de la lista"))
while elementos_lista:
    n = int(input("Ingrese los valores "))
    lista1.append(n)
    elementos_lista += -1
lista2 = lista1
i = 0
for element in lista2:
    if lista2[i] == lista2[i-1]:
        lista2.remove(lista2[i])
        lista2.remove(lista2[i-1])
    i+=1

print("Lista original:",lista1)
print("Lista sin numeros repetidos:",lista2)