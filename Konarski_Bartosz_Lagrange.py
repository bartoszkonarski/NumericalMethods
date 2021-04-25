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