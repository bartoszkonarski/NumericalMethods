import numpy as np
import matplotlib.pyplot as plt

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