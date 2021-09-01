import math
import numpy as np

def Konarski_Bartosz_Jacobi(A, eps):
    n = len(A)
    while (True):
        currentMax = 0
        for x in range(n):
            for y in range(n):
                if x > y:
                    if currentMax <= abs(A[x][y]):
                        currentMax = abs(A[x][y])
                        p = x
                        q = y
        if currentMax < eps:
            break

        if (A[p][p] == A[q][q]):
            theta = np.pi / 4
        else:
            theta = math.atan(A[p][q] * 2 / (A[p][p] - A[q][q])) / 2



        T = np.identity(n)

        T[p][p] = math.cos(theta)
        T[p][q] = -math.sin(theta)
        T[q][p] = math.sin(theta)
        T[q][q] = math.cos(theta)

        T1 = np.identity(n)

        T1[p][p] = math.cos(theta)
        T1[p][q] = math.sin(theta)
        T1[q][p] = -math.sin(theta)
        T1[q][q] = math.cos(theta)

        A = np.dot(np.dot(T1, A), T)



    return A.diagonal()


A = [[5, 4, 1],
     [4, 1, 2],
     [1, 2, 7]]

eps = 0.000001

wynik = Konarski_Bartosz_Jacobi(A, eps)
print(wynik)

