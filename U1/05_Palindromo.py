palindromo = False
lista =[]
elementos_lista = str(input("Ingrese los elementos de la lista"))
lista = list(elementos_lista)
for i in range(0, (int(len(lista)/2))):
    if lista[i] == lista[-i-1]:
        palindromo = True
if palindromo == True:
    print("Es una capicua/palindromo")
else:
    print("No es capicua/palindromo")