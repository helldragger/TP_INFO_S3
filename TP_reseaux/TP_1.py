import matplotlib.pyplot as plt
import numpy as np



def main():
    seq = "10000101111"
    x_nrz = np.arange(0, 11, 1)
    y_nrz = np.array(nrz(seq))
    y_nzi = np.array(nrzi(seq))

    x_man = np.arange(0, 11, 0.5)
    y_man = np.array(manchester(seq))

    plt.figure(0)
    plt.step(x_nrz, y_nrz, 'D-', linewidth=5)

    plt.figure(1)
    plt.step(x_nrz, y_nzi, 'D-', linewidth=5)

    plt.figure(2)
    plt.step(x_man, y_man, 'D-', linewidth=5)

    plt.show()


def nrz(seq):
    res = []
    for char in seq:
        if char == '1':
            res.append(1)
        else:
            res.append(-1)
    return res


def nrzi(seq):
    res = []
    states = [-1, 1]
    state = False
    for char in seq:
        if char == '1':
            state = not state
        res.append(states[int(state)])
    return res


def manchester(seq):
    res = []
    for char in seq:
        if char == '1':
            res.append(1)
            res.append(-1)
        else:
            res.append(-1)
            res.append(1)
    return res


if __name__ == "__main__":
    main()
