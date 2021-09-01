import numpy as np
import matplotlib.pyplot as plt

def Konarski_Bartosz_styczne(f,fd,x0,eps):
    xn = x0
    xp = abs(xn)+2*eps
    while(abs(xn-xp)>=eps):
        fxn = f(xn)
        fdxn = fd(xn)
        if fdxn == 0:
            print('Brak rozwiazań')
            return None
        xp = xn
        xn = xn - fxn / fdxn

    xx = np.linspace(xn-2*xn, xn+2*xn, 100)
    yy = f(xx)
    x = np.linspace(xn - 2 * xn, xn + 2 * xn, 200)
    y = [0 for p in x]
    yp = lambda x: fd(xn)*x+f(xn)-fd(xn)*xn
    plt.plot(xx, yy, 'r-',label="funkcja")
    plt.plot(xn,f(xn),'bo',label=f"uzyskana wartość: {xn}")
    plt.plot(xx,yp(xx),'g-',label="styczna")
    plt.plot(x, y, 'k-')
    plt.legend()
    plt.show()

    return xn

f = lambda x: 2*(x**2)-4*x+2
fd = lambda x: 4*x-4
f2 = lambda x: (x+2)*(x-3)*(x-5)
fd2 = lambda x: 3*(x**2)-12*x-1
print(Konarski_Bartosz_styczne(f,fd,0,0.01))
print(Konarski_Bartosz_styczne(f2,fd2,0,0.01))