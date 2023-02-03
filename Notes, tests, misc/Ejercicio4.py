from random import randrange
lista = [0,0,0,0,0]
for i in range(0, 5):
    lista[i] = randrange(1,11)
    while lista[i-1]==lista[i]:
        lista[i-1] = randrange(1,11)

print(lista)
    