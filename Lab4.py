def Konarski_Bartosz_gauss_jordan(A, b):
    for i in range(len(A) - 1):     #działania pod przekątną
        for j in range(i + 1, len(A)):
            mult = A[j][i] / A[i][i]
            for k in range(i, len(A)):
                A[j][k] = A[j][k] - mult * A[i][k]
            b[j] = b[j] - mult * b[i]

    for i1 in range(1, len(A)):     #działania nad przekątną
        for j1 in range(i1):
            mno1 = A[j1][i1] / A[i1][i1]
            for k1 in range(j1, len(A)):
                A[j1][k1] = A[j1][k1] - mno1 * A[i1][k1]
            b[j1] = b[j1] - mno1 * b[i1]

    output = [0 for x in range(len(A))]
    for index in range(len(output)):
        output[index] = b[index] / A[index][index]
    return output

def Konarski_Bartosz_gauss_pivot(A,b):
    for i in range (len(A)-1):
        current = i
        pivot = A[i][i]
        for x in range(i+1,len(A)):
            if(abs(A[x][i])>abs(pivot)):
                pivot=A[x][i]   #największa do tej pory liczba w danej kolumnie
                current = x     #numer wiersza do zamiany z "pierwszym" w tej pętli

        A[current],A[i] = A[i],A[current]   #zamiany wierszy w macierzy i w wyniku
        b[current],b[i] = b[i],b[current]

        for j in range(i+1,len(A)):     #dalszy ciąg standardowego algorytmu eliminacji Gaussa
            mult = A[j][i]/A[i][i]
            for k in range(i,len(A)):
                A[j][k]=A[j][k]-mult*A[i][k]
            b[j] = b[j]-mult*b[i]
    return Konarski_Bartosz_ukladU(A,b)

def Konarski_Bartosz_ukladU(L, b):
    x = [0 for x in range(len(L))]
    for k in range(len(L)-1,-1,-1):
        sumka = 0
        for element in range(len(L)-1, k,-1):
            sumka += L[k][element] * x[element]
        x[k] = (b[k] - sumka) / L[k][k]
    return x

m1 = [[2, 1, 4], [6, 6, 14], [4, 14, 19]]
b1 = [1, 8, 25]
print(Konarski_Bartosz_gauss_jordan(m1, b1))
m2 = [[2,-3,-1],[-4,10,5],[8,-4,4]]
b2 = [9,-29,12]
print(Konarski_Bartosz_gauss_pivot(m2,b2))