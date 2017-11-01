import numpy as np
import matplotlib.pyplot as mpl
import time as time
import scipy as sc
import scipy.misc as misc


def run():
    vectors()
    functions()
    comparaison()
    matrices()
    image()


def print_vect(v):
    print("Vector:", v)
    print("Size  :", v.shape[0])


def vectors():
    v_0 = np.zeros(5)
    print_vect(v_0)
    v_inc = np.arange(3, 12, 0.5)
    print_vect(v_inc)
    v_squ = np.arange(-5, 5, 1)
    v_squ **= 2
    print_vect(v_squ)
    v_2 = np.arange(0, 17, 1)
    v_2 = 2 ** v_2
    print_vect(v_2)


def functions():
    x = np.arange(0, 2*np.pi, 1e-3)
    y = np.sin(x)
    mpl.plot(x, y, '+-')
    mpl.show()

    x = np.arange(0, 2 * np.pi, (2 * np.pi) / 10)
    y = np.sin(x)
    mpl.plot(x, y, '+-')
    mpl.show()

    x_1 = np.arange(0, 2, 0.01)
    y_1 = x_1
    mpl.plot(x_1, y_1, x_1, y_1 ** 2, x_1, y_1 ** 3)
    mpl.show()


def comparaison():
    t1 = time.time()
    s = 0
    for n in range(100000000):
        s += n
    print(s)
    print("Temps utilisé: ", time.time() - t1)

    t1 = time.time()
    v = np.arange(0, 100e6)
    s = v.sum()
    print(s)
    print("Temps utilisé: ", time.time() - t1)

    t1 = time.time()
    s = (100000000 + 0) * (100000000/2)
    print(s)
    print("Temps utilisé: ", time.time() - t1)


def matrices():
    print_vect(np.zeros((12, 4)))

    print_vect(np.eye(16))

    print_vect(np.array([[1, 31], [51, 12]]))


def image():
    im = misc.ascent()
    mpl.figure(0)
    mpl.imshow(im, cmap="gray", vmin=0, vmax=255)

    mpl.figure(1)
    mpl.imshow(im, cmap="gray", vmin=0, vmax=255)

    mpl.show()

    border = np.zeros(np.array(im.shape) + 100)
    border[50:-50, 50:-50] = im
    mpl.imshow(border, cmap="gray", vmin=0, vmax=255)
    mpl.show()


def contrast():
    im = misc.ascent()
    p_min = 255
    p_max = 0
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            p_min = min(p_min, im[x, y])
            p_max = max(p_max, im[x, y])

