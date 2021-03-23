def Konarski_Bartosz_Horner(a,x):
    output=a[0]
    for factor in a[1:]:
        output = factor+x*output
    return output

#Tutaj wersja jednolinijkowa, bardzo nieczytelna ale tak samo skuteczna
import functools
def hornerOneLine(a,x):
    return functools.reduce(lambda a1,a2:x*a1+a2,a)