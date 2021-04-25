import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

x = np.arange(-6, 6, 1.5)
y = np.arange(-6, 6, 1.5)

X, Y = np.meshgrid(x, y)

# Z musi być na s
Z = np.sin(np.sqrt(X**2+Y**2))

fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(60, 35)

plt.show()


# INTERPOLACJA


f = interp2d(x, y, Z, kind='cubic')

xx = np.arange(-6, 6, 0.1)
yy = np.arange(-6, 6, 0.1)

XX, YY = np.meshgrid(xx, yy)
ZZ = f(xx, yy)

fig2 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ,rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(60, 35)

plt.show()