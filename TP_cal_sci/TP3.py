import math
import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

R=6367.445


def print_vect(vect):
    print(vect.shape)
    print(vect)


coordN = np.loadtxt("data/villes_normandie.csv",
                  delimiter=";",
                  usecols=(11,12),
                  skiprows=1)
print_vect(coordN)

nbv = 300
coord = coordN[nbv]
print_vect(coord)

coord = coord*(np.pi/180)
cgCaen = coord[4]
cgFalaise = coord[81]


def distGeo(cg1, cg2):
    lat1, lon1 = cg1
    lat2, lon2 = cg2
    return R * np.arccos(np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(
        lat2) * np.cos(lon1 - lon2))


print(distGeo(cgCaen, cgFalaise))
vdist=pdist(coord, distGeo)
