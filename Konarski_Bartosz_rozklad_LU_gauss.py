import numpy

def Konarski_Bartosz_rozklad_LU_gauss(A):
    L = numpy.identity(len(A))
    for i in range (len(A)-1):
        for j in range(i+1,len(A)):
            mult = A[j][i]/A[i][i]
            L[j][i] = mult
            for k in range(i,len(A)):
                A[j][k]=A[j][k]-mult*A[i][k]
    U = A
    return U,L.tolist()