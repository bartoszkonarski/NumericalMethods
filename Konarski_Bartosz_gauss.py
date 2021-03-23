def Konarski_Bartosz_ukladU(L, b):
    x = [0 for x in range(len(L))]
    for k in range(len(L)-1,-1,-1):
        sumka = 0
        for element in range(len(L)-1, k,-1):
            sumka += L[k][element] * x[element]
        x[k] = (b[k] - sumka) / L[k][k]
    return x

def Konarski_Bartosz_gauss(A,b):
    for i in range (len(A)-1):
        for j in range(i+1,len(A)):
            mult = A[j][i]/A[i][i]
            for k in range(i,len(A)):
                A[j][k]=A[j][k]-mult*A[i][k]
            b[j] = b[j]-mult*b[i]
    return Konarski_Bartosz_ukladU(A,b)