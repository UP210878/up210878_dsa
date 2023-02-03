calicua = False
lista =[]
elementos_lista = int(input("Ingrese los elementos de la lista"))
while elementos_lista:
    n = int(input("Ingrese los valores "))
    lista.append(n)
    elementos_lista += -1
for i in range(0, (int(len(lista)/2))):
    if lista[i] == lista[-i-1]:
        calicua = True
print("Es un capicua: ", calicua)