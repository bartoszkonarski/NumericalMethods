import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import pchip_interpolate
import matplotlib.pyplot as plt
import sys

# import pylab

# WEZLY INTERPOLACYJNE
x = np.linspace(0, 2, 8)
x = x * np.pi
y = np.sin(x)

# Punkty, w których wyliczamy wartosci funkcji interpolacyjnych
x2 = np.linspace(0, 2, 1000)
x2 = x2 * np.pi

# FUNKCJE SCHODKOWE

f_1 = interp1d(x, y, kind='nearest')

plt.plot(x, y, 'o')

plt.plot(x2, f_1(x2), '-')
plt.legend(['wezly', 'najblizszy'], loc='best')
plt.show()

# sys.exit(0)

f_2 = interp1d(x, y, kind='previous')
f_3 = interp1d(x, y, kind='next')

plt.plot(x, y, 'o')

plt.plot(x2, f_1(x2), '-', x2, f_2(x2), '--', x2, f_3(x2), ':')
plt.legend(['wezly', 'najblizszy', 'poprzedni', 'nastepny'], loc='best')
plt.show()

# sys.exit(0)

# FUNKCJE SKLEJANE - SPLINE

f_1 = interp1d(x, y, kind='slinear')

plt.plot(x, y, 'o', x2, np.sin(x2))
plt.plot(x2, f_1(x2), '-')
plt.legend(['wezly', 'sin(x)', 'liniowy'], loc='best')
plt.show()

# sys.exit(0)


f_2 = interp1d(x, y, kind='quadratic')
f_3 = interp1d(x, y, kind='cubic')

# Dodajemy Piecewise Cubic Hermite Interpolating Polynomial
f_4 = pchip_interpolate(x, y, x2)

plt.plot(x, y, 'o', x2, np.sin(x2))

plt.plot(x2, f_1(x2), '-', x2, f_2(x2), '--', x2, f_3(x2), ':', x2, f_4, '-')
plt.legend(['wezly', 'sin(x)', 'liniowy', 'kwadratowy', 'cubic', 'pchip'], loc='best')
plt.show()

# BŁĄD BEZWZGLĘDNY METOD SPLINE

err_1 = abs(f_1(x2) - np.sin(x2))
err_2 = abs(f_2(x2) - np.sin(x2))
err_3 = abs(f_3(x2) - np.sin(x2))
err_4 = abs(pchip_interpolate(x, y, x2) - np.sin(x2))

plt.plot(x2, err_1, '-', x2, err_2, '--', x2, err_3, ':', x2, err_4, '-')
plt.legend(['liniowy', 'kwadratowy', 'cubic', 'pchip'], loc='best')
plt.show()

# TYLKO WIELOMIANY 3-CIEGO STOPNIA - zachowanie koło maksimum

x2 = np.linspace(0, 1, 500)
x2 = x2 * np.pi

f_4 = pchip_interpolate(x, y, x2)

plt.plot(x[1:4], y[1:4], 'o', x2, np.sin(x2))

plt.plot(x2, f_3(x2), ':', x2, f_4, '-')
plt.legend(['wezly', 'sin(x)', 'cubic', 'pchip'], loc='best')
plt.show()

# TYLKO WIELOMIANY 3-CIEGO STOPNIA - zachowanie dla funkcji płaskiej

x = np.linspace(-3, 3, 7)
y = [-1, -1, -1, 0, 1, 1, 1]

x2 = np.linspace(-3, 3, 1000)

f_3 = interp1d(x, y, kind='cubic')
f_4 = pchip_interpolate(x, y, x2)

plt.plot(x, y, 'o', x2, f_3(x2), '-', x2, f_4, '-.')
plt.legend(['wezly', 'cubic', 'pchip'], loc='best')