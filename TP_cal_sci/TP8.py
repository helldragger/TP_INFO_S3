import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.io.wavfile as wavfile


def add_to_graph(figure, x, y):
    plt.figure(figure)
    plt.plot(x, y)


def draw_graphs():
    plt.show()


def convolution(s, fr):
    f = 1
    x = np.arange(-5, 5, (5-(-5))/2000)
    y1 = np.sin(2 * np.pi * f * x)
    y3 = np.sin(2 * np.pi * 2 * f * x)
    add_to_graph(0, x, y1)
    add_to_graph(1, x, y3)

    draw_graphs()

    y13= (y1+y3)/np.max(y1+y3)
    add_to_graph(0, x, y13)
    draw_graphs()

    y1e = y1 + 0.1* np.random.normal()
    s = 10e-1
    filtrePorte = (np.abs(x) < s).astype(int)
    fr = 1.5
    filtreSinc = np.sinc(2*fr*x)
    add_to_graph(0, x, filtrePorte)
    add_to_graph(1, x, filtreSinc)
    draw_graphs()

    convo_y1e = sc.convolve(y1e, filtrePorte, mode="same")
    convo_y1e /= np.max(convo_y1e)

    add_to_graph(0, x, y1)
    add_to_graph(0, x, convo_y1e)
    draw_graphs()

    convo_y13 = sc.convolve(y13, filtreSinc, mode="same")
    convo_y13 /= np.max(convo_y13)

    add_to_graph(0, x, y1)
    add_to_graph(0, x, convo_y13)
    draw_graphs()


def fundamental(x, parSec, duree, fdo):


    notes = ["do", "do#", "re", "mib", "mi", "fa", "fa#", "sol", "lab","la",
             "sib", "si", "do2"]


    for i in range(len(notes)):
        x = np.arange(0, duree, duree/parSec)
        son = np.sin(2*np.pi*( 2**(i/12)*fdo )*x)
        wavfile.write("data/"+notes[i]+".wav", parSec, 0.8*son/np.max(np.abs(
            son)))


def recup_fund(x, parSec, duree, fdo):
    rate, son = wavfile.read('data/D.wav')
    add_to_graph(0, np.arange(0, son.shape[0]*rate, rate), son)
    draw_graphs()

    x2 = np.arange(-0.05, 0.05, 2*0.05*parSec)
    filtre = np.sinc(2*fdo*x2)
    sonD = sc.convolve(son,filtre,"same")
    #wavfile.write("data/piano2.wav", parSec, 0.8 * son / np.max(np.abs(son)))
    return sonD, rate


def etude(sonD, rate):
    x =  np.arange(0, sonD.shape[0]*rate, rate)
    meanS = np.mean(sonD)
    maxS = np.max(sonD)
    aMax = maxS - meanS

    s = 2*(sonD / aMax)**2
    filtrePorte = (np.abs(x) < 0.01).astype(int)

    a = (sc.convolve(s, filtrePorte, "same"))**0.5
    a /= np.max(a)

    add_to_graph(0, x, sonD)
    add_to_graph(0, x, a)
    draw_graphs()

    add_to_graph(0, x, sonD)
    b = sonD.copy()
    for i in range(a.shape[0]):
        if a[i] > 10e-2:
            b[i] /= a[i]
    add_to_graph(0, x, b)
    draw_graphs()


def reverb(parSec):
    pianoRate, piano = wavfile.read('data/piano.wav')
    salleRate, salle = wavfile.read('data/salle.wav')
    salle = salle[:4 * salleRate, :]
    piano = salle[:4 * pianoRate, :]
    reverb = piano.copy()
    reverb[0] = sc.convolve(piano[0], salle[0], "same")
    reverb[1] = sc.convolve(piano[1], salle[1], "same")
    #wavfile.write("data/reverb.wav", parSec, 0.8 * reverb / np.max(np.abs(
    # reverb)))


def main():
    parSec = 44100
    duree = 3
    fdo = 261.63
    x = np.arange(0, duree, duree/parSec)

    convolution(10e-1, 1.5)
    convolution(10e-1, 3.5)
    fundamental(x, parSec, duree, fdo)
    sonD, rate = recup_fund(x, parSec, duree, fdo)
    etude(sonD, rate)
    reverb(parSec)


main()
