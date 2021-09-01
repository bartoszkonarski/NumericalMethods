import numpy as np
import matplotlib.pyplot as plt


def Konarski_Bartosz_Newton_wielowymiarowy(u, Jac, x0, eps):
    xk = x0
    plt.plot(xk[0],xk[1],'gs')
    xk1 = xk - np.dot(np.linalg.inv(Jac(xk)),u(xk))
    while np.linalg.norm(xk1-xk)>eps:
        xk = xk1
        plt.plot(xk[0], xk[1], 'gs')
        xk1 = xk - np.dot(np.linalg.inv(Jac(xk)),u(xk))

    plt.plot(xk1[0], xk1[1], 'rs')
    print(xk1)
    plt.show()
    return xk1

#PRZYKLAD Z LABORATORIOW
jac = lambda x:np.array([[2*x[0],2*x[1]],[-6*x[0],-1]])
f = lambda x:np.array([x[0]**2+x[1]**2-9,-3*x[0]**2-x[1]])
x = np.linspace(-20.0, 20.0, 1000)
y = np.linspace(-20.0, 20.0, 1000)
X, Y = np.meshgrid(x,y)
F = f([X,Y])[0]
plt.contour(X,Y,F,[0])
F = f([X,Y])[1]
plt.contour(X,Y,F,[0])
Konarski_Bartosz_Newton_wielowymiarowy(f, jac, np.array([1, 0]), 0.0001)

#PRZYKLAD Z CWICZEN
jac = lambda x:np.array([[2*x[0],2*x[1]],[2*x[0],-1]])
f = lambda x:np.array([x[0]**2+x[1]**2-4,x[0]**2-x[1]+2])
x = np.linspace(-20.0, 20.0, 1000)
y = np.linspace(-20.0, 20.0, 1000)
X, Y = np.meshgrid(x,y)
F = f([X,Y])[0]
plt.contour(X,Y,F,[0])
F = f([X,Y])[1]
plt.contour(X,Y,F,[0])
Konarski_Bartosz_Newton_wielowymiarowy(f, jac, np.array([1, 0]), 0.0001)