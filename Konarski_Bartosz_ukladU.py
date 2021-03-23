def Konarski_Bartosz_ukladU(L, b):
    x = [0 for x in range(len(L))]
    for k in range(len(L)-1,-1,-1):
        sumka = 0
        for element in range(len(L)-1, k,-1):
            sumka += L[k][element] * x[element]
        x[k] = (b[k] - sumka) / L[k][k]
    return x