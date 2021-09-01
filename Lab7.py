import matplotlib.pyplot as plt
import numpy as np

def Konarski_Bartosz_Lagrange(x,xw,yw,n):
    def calculate(arg):
        value = 0
        for i in range(n+1):
            m = 1
            for j in range(n+1):
                if i!=j:
                    m*=(arg-xw[j])/(xw[i]-xw[j])
            value+=yw[i]*m
        return value
    return [calculate(xi) for xi in x]

#print(Konarski_Bartosz_Lagrange([50,40,80],[0,20,40,60,80,100],[26,48.6,61.6,71.2,74.8,75.2],5))
#print(Konarski_Bartosz_Lagrange([-1,1,2],[-2,1,4],[5,3,7],2))
print(Konarski_Bartosz_Lagrange([0,1,3],[-2,1,4],[5,3,7],2))