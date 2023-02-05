
from random import randrange

M = int(input("Colummas"))
N = int(input("Filas"))

matrix = [[randrange(1,10) for j in range(M)] for i in range(N)]
matrix_T = [[matrix[j][i] for j in range(N)] for i in range(M)]

for i in range(N):
    print(matrix[i])

print("\n")

for i in range(M):
    print(matrix_T[i])