### PARTIE 1

# Binôme:   PINOT Morine - 21501666
#           JACQUIOT Christopher - 21501785
#
#

import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.ndimage
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

### PARTIE 2

# Question 1: cf. Rapport, partant du principe que le jeu est un jeu de
# dames, nous comptons les cases en diagonale, ainsi la distance apparente
# entre les deux pieces blanches serait de 2 cases en diagonale pure, et de 5
# si on fait le parcours par cases adjacentes

print("Question 1: cf rapport.")

# Question 2:
print("Question 2: Affichage de l'image de départ.")
img = sc.ndimage.imread("dameNB.png")
plt.figure(0)
plt.imshow(img, cmap='gray')
plt.show()


# Question 3:
def hist(im):
    x, h = np.unique(im, return_counts=True)
    plt.fill_between(x, 0, h)
    # normalization from max to 100
    h = h * 100 / np.max(h)
    plt.axis((0, 255, 0, np.max(h)))
    plt.show()


print("Question 3: Affichage de l'histogramme des niveaux de gris.")
plt.figure(1)
hist(img)

# cf. Rapport
# la partie vers 255 est sensée représenter le blanc des pions.


# Question 4:
def seuil(im, x):
    im[im >= x] = 255
    im[im < x] = 0
    return im


print("Question 4: Création de l'image seuillée à 230.")
plt.figure(2)
im_bin = seuil(img.copy(), 230)


# Question 5:
print("Question 5: Affichage de l'image seuillée à 230.")
plt.imshow(im_bin, cmap='gray')
plt.show()

# cf. Rapport
# Les pions sont desormais sur fond noir

### PARTIE 3

# Question 1:
print("Question 6: Récupération des coordonnées entre pixels des pions.")
coords = np.argwhere(im_bin == 255)
print(coords)

# Question 2:
print("Question 7: Calcul des distances entre coordonnées des pixels.")
dist = pdist(coords)
print(dist)

# Question 3:
# la bordure de l'image est de 6 pixels, on retire donc 6*2 de longueur pour
# le calcul du nombre de pixel par case
print("Question 8: Calcul du nb de pixel par case.")

pix_per_case = (img.shape[0] - 6*2) / 10
print(pix_per_case, "pixels per case")

# Question 4:
print("Question 9: Récupération de la distance maximale entre les pixels des "
      "pions.")

dist_in_cases = np.floor(dist / pix_per_case)
max_dist = max(dist_in_cases)
print(max(dist), "pixels")
print(max_dist, "cases")

# cf. Rapport
# C'est une bonne approximation de la distance entre les pions parce que cela
#  mesure la distance diagonale entre les deux pions, qui est la longueur
# d'une droite qui passe par les centres des deux pions.

# Question 5:
print("Question 10: Affichage de l'histogramme des distances entre pixels.")

plt.figure(3)
# Histogramme en pixels
hist(dist)
# Histogramme en cases
# hist(dist_in_cases)

# cf. Rapport
# le premier pic représent les distances des pixels a l'intérieur du meme pion
# le deuxieme pic représente les distances des pixels entre les deux pions

# Question 6:
print("Question 11: Calcul des distances moyennes entre coordonnées des "
      "pixels des deux pions après sélection des distances supérieures à 1 "
      "case.")

dist_btw_pawns = dist[dist > pix_per_case]
avg_dist_btw_pawns = np.mean(dist_btw_pawns)
avg_dist_in_cases = avg_dist_btw_pawns / pix_per_case
print(avg_dist_btw_pawns, "pixels")
print(avg_dist_in_cases, "cases")
# cf. Rapport
# Cette distance est plus petite car elle cherche a récupérer une
# approximation de la distaance entre les deux centres des pions plutot que
# leurs extrémités les plus éloignées.
# Cela se rapproche plutot bien de notre estimation de départ avec 4.3 cases
# de distance.

# Question 7:
print("Question 12: Calcul du diamètre d'un pion a partir du maximum des "
      "distances inférieures à 1 case.")
dist_of_a_pawn = dist[dist < pix_per_case]
diameter_of_a_pawn = max(dist_of_a_pawn)
print(diameter_of_a_pawn, "pixels")
print(diameter_of_a_pawn/pix_per_case, "cases")
