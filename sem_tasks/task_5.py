import numpy as np
import matplotlib.pyplot as plt


def find_polynom(x, y, n, t):
    P_n = 0
    for i in range(n + 1):
        numer = 1
        denomin = 1
        for j in range(n + 1):
            if i != j:
                numer *= t - x[j]
                denomin *= x[i] - x[j]
        P_n += y[i] * numer / denomin
    return P_n


def draw():
    n = 4
    x_k = [(1 + k / n) for k in range(n + 1)]
    y_k = [np.log(x) for x in x_k]
    s = 10 ** 2
    x = [0.5 + i / s * 2 for i in range(s + 1)]
    Lagrange = [find_polynom(x_k, y_k, n, t) for t in x]
    diff = [Lagrange[k] - np.log(x)[k] for k in range(s+1)]
    # plt.plot(x, Lagrange, 'r')
    plt.plot(x, diff)
    # plt.plot(x_k, y_k, 'bo', markersize=4)
    # plt.ylim(-1 / 4, 1)
    # plt.xlim(1 / 2, 5 / 2)
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    draw()


if __name__ == '__main__':
    main()
