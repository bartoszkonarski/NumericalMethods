def Konarski_Bartosz_suma_mac(A, B):
    if (len(A) != len(B) or len(A[0]) != len(B[0])):  #sprawdzenie czy można dodać te macierze
        return False
    output = [[0 for x in range(len(A[0]))] for y in range(len(A))] #utworzenie macierzy z samych 0 o docelowych wymiarach
    for x in range(len(A)):
        for y in range(len(A[0])):
            output[x][y] = A[x][y] + B[x][y]

    return output
