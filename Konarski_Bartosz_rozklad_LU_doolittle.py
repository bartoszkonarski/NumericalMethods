import numpy

def Konarski_Bartosz_rozklad_LU_doolittle(A):
    n = len(A)
    L = numpy.zeros((n,n)).tolist()
    U = numpy.zeros((n,n)).tolist()

    for i in range (n):
        for j in range (i,n):
            suma = 0
            for k in range(i):
                suma += L[i][k]*U[k][j]
            U[i][j] = A[i][j] - suma
        for j in range(i,n):
            if j == i:
                L[i][i] = 1
                continue
            suma = 0
            for k in range(i):
                suma+=L[j][k]*U[k][i]
            L[j][i] = (A[j][i]-suma)/U[i][i]

    return L,U