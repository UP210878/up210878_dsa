from random import randrange
N = int(input("Ingrese el tamano de la matriz"))
lista = [[None for j in range(N)] for i in range(N)]
i = 0
j = 0
repetido = False
while i < N:
    while j <N:
        n = randrange(1,(N**2)+1)
        for k in range(N):
            if n not in lista[k] and n not in lista[i]:
                repetido = False              
            else:
                repetido = True
                break
        if repetido == False:
            lista[i][j] = n
            j = j+1
        else:
            continue
    j = 0
    i=i+1

print(lista)


"""for i in range(0, N):
    for j in range(0, N):
        n = randrange(1,(N**2)+1)
        if n != lista[i-j][j]:
            if n != lista[i][i-j]:
                lista[i][j]=n 
        else:
            continue"""