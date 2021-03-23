def Konarski_Bartosz_silnia(n):
    if n <= 1:
        return 1
    output = 1
    for x in range(2, n + 1):
        output *= x
    return output
