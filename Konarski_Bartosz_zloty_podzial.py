import numpy as np
import matplotlib.pyplot as plt
import math

def Konarski_Bartosz_zloty_podzial(f,a,b,eps):
    aS = a
    bS = b
    p = (math.sqrt(5)-1)/2
    print(p)
    k=1
    while (b-a)**k>eps:
        xl = b-p*(b-a)
        xr = a+p*(b-a)
        if f(xl)>f(xr):
            a=xl
        else:
            b=xr
        k+=1
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
print(Konarski_Bartosz_zloty_podzial(f,-7,18,0.01))