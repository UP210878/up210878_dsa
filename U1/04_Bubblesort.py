lista = []
elementos_lista = int(input("Ingrese cuantos valores de la lista"))
while elementos_lista:
    n = int(input("Ingrese los valores "))
    lista.append(n)
    elementos_lista += -1

print ("Lista original: ", lista)
swapped = True 
while swapped:
    swapped = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            swapped = True 
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("Metodo bubble sort(Orden Ascendente): ", lista)