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