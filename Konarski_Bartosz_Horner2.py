def Konarski_Bartosz_horner(a,c):
    output =[]
    output.append(a[0])
    counter = 1
    while(counter<len(a)):
        output.append(output[counter-1]*c+a[counter])
        counter+=1
    reszta = output.pop()
    return (output,reszta)