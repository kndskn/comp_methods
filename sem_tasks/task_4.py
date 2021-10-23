import matplotlib.pyplot as plt
from math import *

precision = 10 ** 5


def bessel(x, m, t):
    """ Calculates bessel function """
    return 1 / pi * cos(m * t - x * sin(t))


def derBessel (x, m, t, x_0, x_n, n_x):
    """ Calculates derivation of bessel function """
    d_x = (x_n - x_0) / n_x
    return (bessel(x+d_x/2, m, t)-bessel(x-d_x/2, m, t)) / d_x


def sum_bessels(t_0, t_n, n_t, x_0, x_n, n_x):
    """ Calculates sum of two bessel functions
        :return two list of results in different dots"""
    d_t = (t_n - t_0) / n_t
    d_x = (x_n - x_0) / n_x
    listBessel = []
    listderBessel = []
    for i in range(n_x):
        x_i = x_0 + i * d_x
        intBessel = 0
        intderBessel = 0
        for j in range(n_t):
            t_l = t_0 + j * d_t
            t_r = t_0 + (j+1) * d_t
            t_c = (t_l + t_r) / 2
            intBessel += d_t / 6 * (bessel(x_i, 1, t_l) + 4 * bessel(x_i, 1, t_c) + bessel(x_i, 1, t_r))
            intderBessel += d_t / 6 * (derBessel(x_i, 0, t_l, 0, 2*pi, precision) + 4 * derBessel(x_i, 0, t_c, 0, 2*pi, precision) + derBessel(x_i, 0, t_r, 0, 2*pi, precision))
        listBessel.append(intBessel)
        listderBessel.append(intderBessel)
    return listBessel, listderBessel


def draw():
    """ Draws graphs of calculation of sum of two bessel functions"""
    vBessel, vderBessel = sum_bessels(0, pi, 16, 0, 2 * pi, precision)
    sumBessel = [func + der for func, der in zip(vBessel, vderBessel)]
    x = [i / precision * 2 * pi for i in range(precision)]
    plt.plot(x, vBessel, label="The bessel func. J_1")
    plt.plot(x, vderBessel, label="Der. of the bessel func. J_0")
    plt.ylim(-1, 1)
    plt.xlim(0, 2 * pi)
    plt.legend()
    plt.show()
    plt.plot(x, sumBessel, label="Sum of the func. and the der.")
    plt.xlim(0, 2 * pi)
    plt.legend()
    plt.show()


def main():
    draw()


if __name__ == '__main__':
    main()
