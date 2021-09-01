import numpy as np
import matplotlib.pyplot as plt

def Konarski_Bartosz_MNK(x,y,n):
    x = np.array(x)
    y = np.array(y)

    A = np.array([[1] for p in range(len(x))])

    for col in range(1,n+1):
        A = np.hstack((A,[[item**col] for item in x]))
    AT = np.transpose(A)
    a = np.dot(np.linalg.inv(np.dot(AT, A)), np.dot(AT, y))

    fx = lambda x: sum(a[i]*(x**i) for i in range(len(a)))

    xx = np.linspace(np.amin(x)-5,np.amax(x)+5,100)
    yy = fx(xx)
    plt.plot(x,y,'ro',label="Punkty")
    plt.plot(xx,yy,'g',label='Wielomian')
    plt.legend()
    plt.show()