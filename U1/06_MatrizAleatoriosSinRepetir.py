from random import randrange
N = int(input("Ingrese el tamano de la matriz"))
lista = [[0 for j in range(N)] for i in range(N)]
i = 0
j = 0

while i < N:
    while j <N:
        n = randrange(1,(N**2)+1)
        if n != lista[i-j][i]:
            if n != lista [i][i-j]:
                lista[i][j] = n
                j+=1
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