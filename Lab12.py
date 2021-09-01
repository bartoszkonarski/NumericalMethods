import numpy as np
from random import random,uniform

def Konarski_Bartosz_Montecarlo_Naiwna():
    n = 10000
    f = lambda x: np.sin(x)
    a = 0
    b = np.pi
    random_values = [f(random()*np.pi) for _ in range(n)]
    output = (b-a)/n*sum(random_values)
    return output

def Konarski_Bartosz_Montecarlo_ChybilTrafil():
    n = 10000
    f = lambda x: np.sin(x)
    k = 0
    a = 0
    b = np.pi
    miny = 0
    maxy = 1
    for proba in range(n):
        valuex = random()*np.pi
        valuey = random()
        if f(valuex)>=0:
            if f(valuex)>=valuey and valuey>0:
                k+=1
        else:
            if f(valuex) < valuey and valuey < 0:
                k-=1
    return k/n*(b-a)*(maxy-miny)

def Konarski_Bartosz_Pole_Kola(r):
    n = 1000000
    czyTrafił = lambda x,y,r: (x**2+y**2)**0.5<=r
    bok = 2*r
    zakres = bok**2
    k = 0
    for proba in range(n):
        x = uniform(-r,r)
        y = uniform(-r,r)
        if czyTrafił(x,y,r):
            k+=1
    return k/n*zakres

print(Konarski_Bartosz_Montecarlo_Naiwna())
print(Konarski_Bartosz_Montecarlo_ChybilTrafil())
print(Konarski_Bartosz_Pole_Kola(1))