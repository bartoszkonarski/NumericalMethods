def Konarski_Bartosz_ukladL(L, b):
    x = [0 for x in range(len(L))]
    for k in range(len(L)):
        sumka = 0
        for element in range(0, k):
            sumka += L[k][element] * x[element]
        x[k] = (b[k] - sumka) / L[k][k]
    return x