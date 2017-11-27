import numpy as np
import matplotlib.pyplot as plt

coord_villes = np.load('data/coord_villes.npy')
d_villes = np.load('data/d_villes.npy')

print(coord_villes)
plt.scatter(coord_villes[:, 0],
            -coord_villes[:, 1],
            color='b',
            marker='s',
            s=5,
            alpha=0.1)
#  plt.show()
n = coord_villes.shape[0]

infect = np.random.rand(n)
villes_src = np.zeros(n)
villes_src = infect < 1 / 500

plt.scatter(coord_villes[villes_src, 0],
            -coord_villes[villes_src, 1],
            color='r',
            marker='s',
            s=5,
            alpha=1)
s = 4
nouvelle_ville_contamine_valeur = s * np.random.normal(0.5,
                                                       0.1,
                                                       d_villes.shape[0])

nouvelle_ville_contamine = nouvelle_ville_contamine_valeur > d_villes


def propager(villes_src):
    nouvelle_ville_contamine = nouvelle_ville_contamine_valeur > d_villes

    ville_source_col = villes_src.reshape((-1, 1))
    return np.sum(nouvelle_ville_contamine * ville_source_col, axis=0) >= 1


nouvelle_ville_contamine = propager(villes_src)

plt.scatter(coord_villes[nouvelle_ville_contamine, 0],
            -coord_villes[nouvelle_ville_contamine, 1],
            color='g',
            marker='s',
            s=5,
            alpha=1)


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

points = np.zeros((0, 2))

fig = plt.figure()


def updatefig(x):
    fig.clear()
    global villes_src
    global nouvelle_ville_contamine

    villes_src = nouvelle_ville_contamine
    nouvelle_ville_contamine = propager(villes_src)

    plt.scatter(coord_villes[:, 0],
                -coord_villes[:, 1],
                color='b',
                marker='s',
                s=5,
                alpha=0.2)

    plt.scatter(coord_villes[villes_src, 0],
                -coord_villes[villes_src, 1],
                color='r',
                marker='s',
                s=5,
                alpha=1)

    plt.scatter(coord_villes[nouvelle_ville_contamine, 0],
                -coord_villes[nouvelle_ville_contamine, 1],
                color='g',
                marker='s',
                s=5,
                alpha=1)
    plt.draw()

anim = animation.FuncAnimation(fig, updatefig, 20)
anim.save("test.mp4", fps=5)
