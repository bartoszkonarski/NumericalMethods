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