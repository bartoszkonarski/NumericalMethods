def Konarski_Bartosz_mnoz_mac(A, B):
    def WymnozPole(x, y, A, B):
        suma = 0
        for item in range(len(A[0])):
            suma += A[x][item] * B[item][y]
        return suma

    if (len(A) != len(B[0])): #sprawdzenie czy można wymnozyć te macierze
        return False
    output = [[0 for x in range(len(A))] for y in range(len(A))] #utworzenie macierzy z samych 0 o docelowych wymiarach
    for x in range(len(output)):
        for y in range(len(output[0])):
            output[x][y] = WymnozPole(x, y, A, B)

    return output
