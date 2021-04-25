import matplotlib.pyplot as plt
import numpy as np
B1x = [x for x in range(5,14,1)]
B1y = [0,0.25,0.5,0.75,1,0.75,0.5,0.25,0]

B2x = [x for x in range(9,18,1)]
B2y = [0,0.25,0.5,0.75,1,0.75,0.5,0.25,0]

Ac_resx = [x for x in range(5,18,1)]
Ac_resy = [0,0.25,0.25,0.25,0.25,0.25,0.5,0.75,0.75,0.75,0.5,0.25,0]
print(B1x)
print(len(B1x), len(B1y))

plt.plot(B1x,B1y,'go-',label='B1', linewidth=5, markersize=12)
plt.plot(B2x,B2y,'bo-',label='B2', linewidth=5, markersize=12)
plt.plot(Ac_resx,Ac_resy,'rD-',label='Ac_res', linewidth=4, markersize=11)
plt.xticks(range(5,18,1))
plt.yticks(np.arange(0,1.25,0.25))
plt.grid()
plt.xlabel('y',loc='right')
plt.ylabel('μ(y)',rotation=0,loc='top')
plt.legend()
plt.show()
