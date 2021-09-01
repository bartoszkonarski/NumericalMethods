import numpy as np
import matplotlib.pyplot as plt

def Konarski_Bartosz_sieczne(f,x1,x2,eps):
    xs = []
    xn2 = x2
    xn1 = x1
    xn = (f(xn2)*xn1-f(xn1)*xn2)/(f(xn2)-f(xn1))
    xs+=[xn2,xn1,xn]
    while (abs(xn - xn1) >= eps):
        if xn2==xn1: return None

        xn2 = xn1
        xn1 = xn
        xn = (f(xn2) * xn1 - f(xn1) * xn2) / (f(xn2) - f(xn1))
        xs.append(xn)

    xs.remove(xn)
    xx = np.linspace(min(xs) - 5, max(xs) + 5, 2000)
    yy = f(xx)
    x = np.linspace(min(xs) -10, max(xs) +10, 10)
    y = [0 for p in x]

    plt.plot(xx, yy, 'r-', label="Funkcja",linewidth=3)
    ys = [f(x) for x in xs]
    plt.plot(xs,ys,'gs',label=f"Uzyskane sieczne",linewidth=1)
    for i in range(len(xs)-1):
        a = (f(xs[i])-f(xs[i+1]))/(xs[i]-xs[i+1])
        b = f(xs[i])-a*xs[i]
        fs = lambda x: a*x+b
        plt.plot(xx,fs(xx),'g--')
    plt.plot(x, y, 'k-')

    plt.plot([x1, x2], [f(x1), f(x2)], 'yo', label=f"Podane punkty: {x1}, {x2}", markersize=7)
    plt.plot(xn, f(xn), 'bo', label=f"Uzyskana wartość: {xn}", markersize=10)
    plt.legend()
    plt.show()

    return xn
f = lambda x : x**3-2*x**2-2
print(Konarski_Bartosz_sieczne(f,1,2,0.02))