from random import randrange
import numpy as np

M1 = int(input("Colummas de primera matriz"))
N1 = int(input("Filas de primera matriz"))

M2 = int(input("Colummas de segunda matriz"))
N2 = int(input("Filas de segunda matriz"))

if N1 != M2:
    print ("No son multiplicables")

matrix1 = [[randrange(0,5) for j in range(M1)] for i in range(N1)]
matrix2 = [[randrange(0,5) for j in range(M2)] for i in range(N2)]

matrix_Total = [[(np.sum(matrix1[i][j]*matrix2[j][i]) for k in range(M1)) for j in range(M1)] for i in range(N2)]

print(matrix1)
print(matrix2)
print(matrix_Total)