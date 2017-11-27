import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as scmisc


def tp6_calcul_derivee():
    # augmentation du nombre de points pour une courbe plus jolie :D
    x = np.arange(-np.pi, np.pi, 10e-3)
    fx = np.sin(x)
    #plt.figure(0)
    #plt.plot(x, fx)

    #plt.figure(1)
    #plt.plot(x, scmisc.derivative(np.sin, x, dx=10e-6))

    #plt.figure(2)
    #plt.plot(x, np.gradient(np.sin(x)))

    df = np.gradient(fx)
    #plt.figure(3)
    #plt.plot(x, df)
    #plt.show()

    return (x, fx, df)


def tp6_analyse_derivee(x, fx, df):
    i = (np.arange(0, x.shape[0], 1) % 3) == 0
    x3 = x[i]
    fx3 = fx[i]
    df3 = df[i]

    plt.plot(x3, fx3)
    plt.quiver(x3, fx3, df3, 0)
    plt.show()


    plt.plot(x3[df3 < 0], fx3[df3 < 0])
    plt.quiver(x3[df3 < 0], fx3[df3 < 0], df3[df3 < 0], 0)
    plt.show()

    return


x, fx, df = tp6_calcul_derivee()
tp6_analyse_derivee(x, fx, df)