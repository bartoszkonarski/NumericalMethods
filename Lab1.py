import math
import numpy


def Konarski_Bartosz_silnia(n):
    if n <= 1:
        return 1
    output = 1
    for x in range(2, n + 1):
        output *= x
    return output


def Konarski_Bartosz_suma_mac(A, B):
    output = [[0 for x in range(len(A[0]))] for y in range(len(A))]
    if (len(A) != len(B) or len(A[0]) != len(B[0])):
        return False
    for x in range(len(A)):
        for y in range(len(A[0])):
            output[x][y] = A[x][y] + B[x][y]

    return output





def Konarski_Bartosz_mnoz_mac(A, B):
    def WymnozPole(x, y, A, B):
        suma = 0
        for item in range(len(A[0])):
            suma += A[x][item] * B[item][y]
        return suma

    if (len(A) != len(B[0])):
        return False
    output = [[0 for x in range(len(A))] for y in range(len(A))]
    for x in range(len(output)):
        for y in range(len(output[0])):
            output[x][y] = WymnozPole(x, y, A, B)

    return output


print(Konarski_Bartosz_silnia(3))
print("===============")
a = [[1, 2], [3, 4],[1,1]]
b = [[4, 3,1], [2, 1,1]]

A = [[1,2],[3,4]]
B = [[4,3],[2,1]]

print(Konarski_Bartosz_suma_mac(a, b))
print(Konarski_Bartosz_suma_mac(A, B))
print("===============")
print(Konarski_Bartosz_mnoz_mac(a, b))
print(Konarski_Bartosz_mnoz_mac(A, B))

