import numpy as np
from numpy.linalg import norm

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