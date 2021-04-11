import numpy
import math

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


# m1 =[[1,2,3],[4,5,6],[7,8,19]]
#
# wynik = Konarski_Bartosz_rozklad_LU_gauss(m1)
# print(wynik[0])
# print(wynik[1])

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

# m2 = [[4,3,2],[8,7,6],[4,7,13]]
#
# wynik = Konarski_Bartosz_rozklad_LU_doolittle(m2)
# print(wynik[0])
# print(wynik[1])

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

m3 = [[4,2,2],[2,5,3],[2,3,6]]

wynik = Konarski_Bartosz_rozklad_cholesky(m3)
print(wynik[0])
print(wynik[1])