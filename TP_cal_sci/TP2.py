"""
Histogramme:
np unique retourne deux vecteurs:
 x, le vecteur contenant chaque valeur qui apparait sur la matrice,
 h, le vecteur qui specifie le nombre d'occurence pour chacune de ces valeurs

fill_between va remplir l'aire entre chaque valeur de 0 et h, aux abscisse x
 il manque plt.show() pour afficher l'histogramme
 D'apres le diagramme, l'image as une majorité grise neutre, et plus de points sombres que blancs.
"""
import numpy as np
import scipy as sc
import scipy.misc as misc
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt


def hist(im):
    x, h = np.unique(im, return_counts=True)
    plt.fill_between(x, 0, h)
    plt.axis((0, 255, 0, np.max(h)))
    plt.show()


def saturate(im, n):
    im[im > 255 - n] = 255
    im[im <= 255 - n] += n
    return im

def desaturate(im, n):
    im[im < n] = 0
    im[im >= n] += n
    return im


def spread(im):
    p_max, p_min = np.max(im), np.min(im)
    return (255*((im[:, :] - p_min) / (p_max - p_min)))//1

def contrast(im):
    return


def run():
    im = ndimage.imread('pics/face_gris.png')
    hist(np.copy(im))
    hist(saturate(np.copy(im), 100))
    hist(spread(np.copy(im)))
    hist(saturate(np.copy(im), 50))
    hist(spread(np.copy(im)))
    hist(desaturate(np.copy(im), 50))
    hist(spread(np.copy(im)))
    plt.imshow(im, cmap='gray', vmin = 0, vmax = 255)
    #plt.imshow(spread(np.copy(im)), cmap='gray', vmin = 0, vmax = 255)
    hist(np.copy(im))
    hist((0.5 * np.cos((1 - np.copy(im)) * 3.14)) + 0.5 )
    hist(np.copy(im) // 255)
    hist((0.5 * np.cos((1 - (np.copy(im) // 255)) * 3.14)) + 0.5)
    hist(((0.5 * np.cos((1 - (np.copy(im) // 255)) * 3.14)) + 0.5) * 255)
    print("finished")




run()
