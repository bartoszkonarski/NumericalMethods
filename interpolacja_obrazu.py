import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("Banach.jpg") # wczytuje obraz z pliku
# konwersja do szarej skali kolorów (greyscale)
im = np.array(im.convert('L'))

# odczytuje liczbę wierszy i kolumn piksli obrazu
nx, ny = im.shape[1], im.shape[0]
# tworzę siatkę kartezjańską piksli obrazu
X, Y = np.meshgrid(np.arange(0, nx, 1), np.arange(0, ny, 1))

# liczba probek piksli z obrazu
nprobek = 99000

# losuje "nprobek" piksli z obrazu
ix = np.random.randint(im.shape[1], size=nprobek)
iy = np.random.randint(im.shape[0], size=nprobek)
# pobieram wartosci wylosowanych piksli
probki = im[iy,ix]
# tworze wykres interpolowany na podstawie wylosowanych piksli
# metody do zastosowania: #linear, #nearest, #cubic
int_im = griddata((iy, ix), probki, (Y, X),method='nearest')

plt.imshow(int_im, cmap=plt.get_cmap('Greys_r'))
plt.show()