import numpy as np
import matplotlib.pyplot as plt
import math

def Konarski_Bartosz_bisekcja(f,a,b,eps):
    if f(a) * f(b) >= 0:
        return None
    start = a
    end = b
    fp = f((start + end) / 2)+2*eps
    while(True):
        m = (start + end) / 2
        fm = f(m)
        if f(start) * fm < 0:
            end = m
        elif f(end) * fm < 0:
            start = m
        elif fm == 0:
            print("Dokładne rozwiązanie!")
            break
        else: return None
        if(abs(fp-fm)<eps): break
        else: fp=fm

    xx = np.linspace(a-2,b+2,100)
    x = np.linspace(a-2-a/2-2,b+2+b/2+2,200)
    yy = f(xx)
    y = f(x)
    plt.plot(xx,yy,'r-',label="funkcja")
    plt.plot(x,[0 for p in x],'k-')
    plt.plot([0 for p in y],y,'k-')
    plt.plot(m,f(m),'bo',label=f"uzyskana wartość: {m}")
    plt.xlim(left=x[0])
    plt.xlim(right=x[-1])
    plt.ylim(top=y[-1])
    plt.ylim(bottom=y[0])
    plt.legend()
    plt.show()
    return m

f = lambda x: -x**3-2*x**2+x+15
f2 = lambda x: x**3-1
f3 = lambda x: math.sin(x)

# print(Konarski_Bartosz_bisekcja(f,1,4,0.01))
# print(Konarski_Bartosz_bisekcja(f2,0,4,0.01))

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
# print(Konarski_Bartosz_styczne(f,fd,0,0.01))
# print(Konarski_Bartosz_styczne(f2,fd2,0,0.01))

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

    plt.plot(xx, yy, 'r-', label="Funkcja")


    print(xs)
    ys = [f(x) for x in xs]
    plt.plot(xs,ys,'go',label=f"Uzyskane sieczne")
    for i in range(len(xs)-1):
        a = (f(xs[i])-f(xs[i+1]))/(xs[i]-xs[i+1])
        b = f(xs[i])-a*xs[i]
        fs = lambda x: a*x+b
        plt.plot(xx,fs(xx),'g--')
    plt.plot(x, y, 'k-')

    plt.plot([x1, x2], [f(x1), f(x2)], 'ys', label=f"Podane punkty: {x1}, {x2}", markersize=7)
    plt.plot(xn, f(xn), 'bs', label=f"Uzyskana wartość: {xn}", markersize=10)
    plt.legend()
    plt.show()

    return xn
f = lambda x : x**3-2*x**2-2
# print(Konarski_Bartosz_sieczne(f,1,2,0.02))


def Konarski_Bartosz_newtod2d(u,Jac,x0,eps):
    xk = x0.transpose()
    jakobian = Jac(xk)
    wartosci = u(xk)
    jakobianodw = np.linalg.inv(jakobian)
    xk1 = xk - np.dot(jakobianodw,wartosci)
    while np.linalg.norm(xk1-xk)>eps:
        xk = xk1
        jakobian = Jac(xk)
        wartosci = u(xk)
        jakobianodw = np.linalg.inv(jakobian)
        xk1 = xk - np.dot(jakobianodw, wartosci)
    return xk1

jac = lambda x:np.array([[2*x[0],2*x[1]],[2,-2*x[0]]])
f = lambda x:np.array([x[0]**2+x[1]**2-3,-x[0]**2+2*x[1]])
print(Konarski_Bartosz_newtod2d(f,jac,np.array([1,0]),0.01))

