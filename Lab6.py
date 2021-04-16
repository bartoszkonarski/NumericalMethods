import numpy as np
from numpy.linalg import norm


def Konarski_Bartosz_jacobi(A, b, eps):

    n = len(A)

    A = np.array(A)
    for i in range(n):
        if(A[i,i]<=(sum(A[i,j] for j in range(n)))-A[i,i]):
            return False
    x0 = np.zeros(n)
    xk = x0.copy()
    xk1 = x0.copy()

    roznica = eps + 1

    while (roznica > eps):

        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i, j] * xk[j]

            xk1[i] = (b[i] - suma) / A[i, i]

        roznica = norm(xk1 - xk, 2)

        xk = xk1.copy()

    return xk1


def Konarski_Bartosz_seidel(A, b, eps):
    n = len(A)

    A = np.array(A)
    for i in range(n):
        if (A[i, i] <= (sum(A[i, j] for j in range(n))) - A[i, i]):
            return False
    x0 = np.zeros(n)
    xk = x0.copy()
    xk1 = x0.copy()
    LD = np.tril(A,k=0)
    U = np.triu(A,k=1)

    roznica = eps + 1

    while (roznica > eps):

        xk1= np.dot(-np.linalg.inv(LD)*U,xk)+np.dot(np.linalg.inv(LD),b)

        roznica = norm(xk1 - xk, 2)

        xk = xk1.copy()

    return xk1


m1 = [[-2, 2, 1], [1, 3, 2], [1, -2, 0]]
m2 = [[3, -2, 1], [1, -3, 2], [-1, 2, 4]]
m3 = [[3, -1, 1], [1, 4, 1], [1, 1, 3]]
m4 =[[4,2,0],[1,2,1],[0,2,4]]
b3 = [5, 6, 5]
b4 = [2,1,0]
eps3 = 0.02
print(Konarski_Bartosz_jacobi(m3, b3, eps3))
print(Konarski_Bartosz_seidel(m3,b3,eps3))
