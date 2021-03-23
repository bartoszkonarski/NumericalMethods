def Konarski_Bartosz_heron(a, x, eps):
    x1=0.5*(x+a/x)
    while abs(x1-x)>eps:
        x,x1=x1,0.5*(x1+a/x1)
    return x1