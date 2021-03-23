import math
import numpy
import functools
def Pochodna():
    h = 1
    wynik = ["krok","iloraz","h","poch"]

    for k in range(40):
        iloraz = (math.exp(10+h)-math.exp(10))/h
        zapis = [k,iloraz,h,math.exp(10)]
        wynik = numpy.vstack([wynik,zapis])
        h=h/2

    return wynik

def Konarski_Bartosz_heron(a, x, eps):
    x1=0.5*(x+a/x)
    while abs(x1-x)>eps:
        x,x1=x1,0.5*(x1+a/x1)
    return x1

def Konarski_Bartosz_Horner(a,x):
    output=a[0]
    for factor in a[1:]:
        output = factor+x*output
    return output

def Konarski_Bartosz_horner(a,c):
    output =[]
    output.append(a[0])
    counter = 1
    while(counter<len(a)):
        output.append(output[counter-1]*c+a[counter])
        counter+=1
    reszta = output.pop()
    return (output,reszta)

def hornerOneLine(a,x):
    return functools.reduce(lambda a1,a2:x*a1+a2,a)



print(Konarski_Bartosz_heron(9, 5, 0.0001))
print(Konarski_Bartosz_Horner([-7,21,-53,12],4))
print(hornerOneLine([-7,21,-53,12],4))
print(hornerOneLine([-3,12],5))
print(Konarski_Bartosz_horner([17,21,-53,12],-4))