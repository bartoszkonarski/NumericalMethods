import numpy as np
import matplotlib.pyplot as plt
import math

def Konarski_Bartosz_zloty_podzial(f,a,b,eps):
    aS = a
    bS = b
    p = (math.sqrt(5)-1)/2
    print(p)
    while (b-a)>eps:
        xl = b-p*(b-a)
        xr = a+p*(b-a)
        if f(xl)>f(xr):
            a=xl
        else:
            b=xr
    xl = b - p * (b - a)
    xr = a + p * (b - a)

    xx = np.linspace(aS-5,bS+5,1000)
    yy = f(xx)
    plt.plot(xx,yy,'r-',label='Wykres funkcji')
    ay = np.linspace(np.min(yy), f(aS), 100)
    ax = [aS for x in range(100)]
    by = np.linspace(np.min(yy), f(bS), 100)
    bx = [bS for x in range(100)]
    plt.plot(ax, ay, 'g-')
    plt.plot(bx, by, 'g-',label='Punkty startowe')
    if f(xl)>f(xr):
        plt.plot(xr,f(xr),'bo',label=f'Obliczone minimum: {xr}')
        output=xr
    else:
        plt.plot(xl, f(xl), 'bo',label=f'Obliczone minimum: {xl}')
        output = xl
    plt.legend()
    plt.show()
    return output


f = lambda x:(x-2)*(x+3)*(x-4)
# print(Konarski_Bartosz_zloty_podzial(f,-5,18,0.01))

def Konarski_Bartosz_prostokaty(f,a,b,n):
    h = (b-a)/(n-1)
    lewy = a
    suma = 0
    for i in range(1,n):
        prawy = a+i*h
        points= [[lewy,0],[lewy,f(lewy)],[prawy,f(lewy)],[prawy,0],[lewy,0]]
        plt.plot([point[0] for point in points],[point[1] for point in points],'b-')
        suma+=f(lewy)
        lewy=prawy
    suma*=h
    xx = np.linspace(a-2,b+2,1000)
    yy=f(xx)
    plt.plot(xx,yy,'r-',label='Wykres funkcji')
    ax = [a for i in range(100)]
    bx = [b for i in range(100)]
    ay = np.linspace(np.min(yy)-1,np.max(yy)+1,100)
    plt.plot(ax,ay,'g-',label='Granice całkowania')
    plt.plot(bx,ay,'g-')
    plt.legend()
    plt.show()
    return suma

f = lambda x:(x-2)*(x+3)*(x-4)
print(Konarski_Bartosz_prostokaty(f,-1,5,90))

def Konarski_Bartosz_trapezy(f,a,b,n):
    h = (b-a)/(n-1)
    lewy = a
    suma = 0
    xx = np.linspace(a - 2, b + 2, 1000)
    yy = f(xx)
    plt.plot(xx, yy, 'r-')
    for i in range(1,n):
        prawy = a+i*h
        points= [[lewy,0],[lewy,f(lewy)],[prawy,f(prawy)],[prawy,0],[lewy,0]]
        plt.plot([point[0] for point in points],[point[1] for point in points],'b-')
        suma+=(f(lewy)+f(prawy))/2
        lewy=prawy
    suma*=h

    ax = [a for i in range(100)]
    bx = [b for i in range(100)]
    ay = np.linspace(np.min(yy)-1,np.max(yy)+1,100)
    plt.plot(ax,ay,'g-')
    plt.plot(bx,ay,'g-')

    plt.show()
    return suma

f = lambda x:(x-2)*(x+3)*(x-4)
print(Konarski_Bartosz_trapezy(f,-1,5,50))