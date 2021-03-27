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