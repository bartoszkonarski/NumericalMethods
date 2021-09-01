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
    # plt.ylim(top=np.amax(y)*1.50,bottom=-abs(np.amin(y))*10)
    plt.legend()
    plt.show()

Konarski_Bartosz_MNK([1,2,4,5,3,5,6,11,15,25,-5],[2,3,7,3,7,11,1,3,9,40,-90],3)
# Konarski_Bartosz_MNK([1,2,3],[2,4,6],2)