import numpy as np
import matplotlib.pyplot as plt

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
f3 = lambda x: np.sin(x)

print(Konarski_Bartosz_bisekcja(f,1,4,0.01))
print(Konarski_Bartosz_bisekcja(f2,0,4,0.01))
print(Konarski_Bartosz_bisekcja(f3,1,4,0.001))