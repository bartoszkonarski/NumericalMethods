import numpy
import math

def Konarski_Bartosz_rozklad_cholesky(A):
    n = len(A)
    L = numpy.zeros((n,n)).tolist()
    U = numpy.zeros((n,n)).tolist()

    for i in range(n):
        for j in range(i,n):
            if(j==i):
                suma = sum(L[i][k]**2 for k in range(i))
                L[i][i] = U[i][i] = math.sqrt(A[i][i]-suma)
            else:
                suma = sum(L[j][k] *L[i][k] for k in range(i))
                L[j][i]= U[i][j] = (A[j][i]-suma)/L[i][i]

    return L,U