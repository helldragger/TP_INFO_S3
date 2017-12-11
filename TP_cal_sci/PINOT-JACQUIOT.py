### PARTIE 0

# Binôme:   PINOT Morine - 21501666
#           JACQUIOT Christopher - 21501785
#
#

import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.ndimage
import scipy.optimize
import scipy.interpolate

### PARTIE 1

#### Question 1

im = scipy.ndimage.imread("pics/im.png")

#### Question 2

plt.imshow(im, cmap='gray', vmin=0, vmax=255)
plt.show()
#### Question 3

p_out = np.asarray([[1, 0], [1, 1], [0, 1], [0, 0]])

#### Question 4
p_out = -1 + 2 * p_out

#### Question 5

coin_r = np.argwhere(
    (im[:, :, 0] == 255) * (im[:, :, 1] == 0) * (im[:, :, 2] == 0))

#### Question 6

coin_c = np.argwhere(
    (im[:, :, 0] == 0) * (im[:, :, 1] == 255) * (im[:, :, 2] == 255))
coin_v = np.argwhere(
    (im[:, :, 0] == 0) * (im[:, :, 1] == 255) * (im[:, :, 2] == 0))
coin_b = np.argwhere(
    (im[:, :, 0] == 0) * (im[:, :, 1] == 0) * (im[:, :, 2] == 255))

#### Question 7

p_in = np.eye(4, 2)

p_in[0] = coin_c
p_in[1] = coin_v
p_in[2] = coin_b
p_in[3] = coin_r

#### Question 8

p_in = -1 + 2 * (p_in / im.shape[0])

#### Question 9

p_in = np.append(p_in, np.zeros((4, 1)), axis=1)


### PARTIE 2

#### Question 1 & 2

def loss(W, X_in, X_out):
    if W.shape[0] == 6:
        W = np.reshape(W, (3, 2))
    return np.sum((X_out - np.matmul(X_in, W)) ** 2, axis=(0, 1))


#### Question 3


v = np.random.uniform(0, 1, (3, 2))
W = scipy.optimize.minimize(lambda W, X_in=p_in, X_out=p_out: loss(W, X_in,
                                                                   X_out), v)

#### Question 4

W = np.reshape(W.x, (3, 2))

#### Question 5

m = np.matmul(p_in, W)
print("Is p_out and p_inW are equal: ")
print(np.equal(p_out, m))

print("=== ===p_out=== ===")
print(p_out)
print("=== ===p_inW=== ===")
print(m)

#
# Nous avvons du négtatif là ou nous voulons.
#

### Partie 3

#### Question 1
x = np.linspace(-1, 1, im.shape[0])
y = np.linspace(-1, 1, im.shape[1])
xv, yv = np.meshgrid(x, y)
X = np.append(xv.reshape(-1)[:, np.newaxis], yv.reshape(-1)[:, np.newaxis],
              axis=1)

#### Question 2

X = np.append(X, np.zeros((X.shape[0], 1)), axis=1)  # ajouter une colonne de 1
#  à X
# comme dans la question 2.1.8


#### Question 3

newX = np.matmul(X,
                 W)  # calculer les new coordonnées des pixel en appliquant la
# formule
# suivante XW, comme dans la question 2.2.5

#### Question 4

indice = np.arange(0, im.shape[0]*im.shape[1])

#### Question 5

indice = indice[np.abs(newX[:, 0] < 1) * (np.abs(newX[:, 1]) < 1)]

#### Question 6



# d = la racine entière de la quantité de nouvelles coordonnées à l'indice
d = int(np.sqrt(len(newX[indice])))
# on arrondis les
pixel_in = np.around((im.shape[0] - 1) * (X[indice] + 1) / 2).astype('int')
pixel_out = np.around((d - 1) * (newX[indice] + 1) / 2).astype('int')
newIm1 = 255 * np.ones((d + 1, d + 1, 3), dtype='uint8')
newIm1[pixel_out[:, 0], pixel_out[:, 1], :] = im[pixel_in[:, 0], pixel_in[:, 1],
                                              :]

#### Question 7
plt.imshow(newIm1)

plt.show()
#### Question 8
d = int(np.sqrt(len(newX[indice])) * 0.75)
pixel_in = np.around((im.shape[0] - 1) * (X[indice] + 1) / 2).astype('int')
pixel_out = np.around((d - 1) * (newX[indice] + 1) / 2).astype('int')
newIm2 = 255 * np.ones((d + 1, d + 1, 3), dtype='uint8')
newIm2[pixel_out[:, 0], pixel_out[:, 1], :] = im[pixel_in[:, 0], pixel_in[:, 1],
                                              :]

plt.imshow(newIm2)
plt.show()

#### Question bonus

#newIm3 = scipy.interpolate.griddata(im.shape, X, newX)

#plt.imshow(newIm3)
#plt.show()
