# Zadanie 1: algorytm do rozwiązywania układu równań L*x = b

def Konarski_Bartosz_ukladL(L, b):
    x = [0 for x in range(len(L))]
    for k in range(len(L)):
        sumka = 0
        for element in range(0, k):
            sumka += L[k][element] * x[element]
        x[k] = (b[k] - sumka) / L[k][k]
    return x

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

#
m1 = [[-2,0,0],[1,3,0],[4,2,2]]
b1 = [2,5,2]

m2 = [[3,-4,3],[0,2,3],[0,0,-2]]
b2 = [23,2,-4]


m3 = [[2,-3,-1],[-4,10,5],[8,-4,4]]
b3 = [9, -29, 12]

print(Konarski_Bartosz_ukladL(m1,b1))
print(Konarski_Bartosz_ukladU(m2,b2))
print(Konarski_Bartosz_gauss(m3,b3))