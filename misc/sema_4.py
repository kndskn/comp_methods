from matplotlib import pyplot as plt
import math


# functions
def Bessel(x, m, t):
    return 1 / math.pi * math.cos(m * t - x * math.sin(t))


def Simpson(t_0, t_n, n_t, x_0, x_n, n_x):
    d_t = (t_n - t_0) / n_t
    d_x = (x_n - x_0) / n_x
    listBessel = []
    listderBessel = []
    for i in range(n_x):
        x_i = x_0 + i * d_x
        intBessel = 0
        intderBesselp = 0
        intderBesseln = 0
        for j in range(n_t):
            t_l = t_0 + j * d_t
            t_r = t_0 + (j + 1) * d_t
            t_c = (t_l + t_r) / 2
            intBessel += d_t / 6 * (Bessel(x_i, 1, t_l) + 4 * Bessel(x_i, 1, t_c) + Bessel(x_i, 1, t_r))

            intderBesselp += d_t / 6 * (Bessel(x_i, 0, t_l) + 4 * Bessel(x_i, 0, t_c) + Bessel(x_i, 0, t_r))
            intderBesseln += d_t / 6 * (Bessel(x_i + d_x, 0, t_l) + 4 * Bessel(x_i + d_x, 0, t_c) +
                                        Bessel(x_i + d_x, 0, t_r))
        intderBessel = (intderBesseln - intderBesselp) / d_x
        listBessel.append(intBessel)
        listderBessel.append(intderBessel)
    return listBessel, listderBessel


# main body

precision = 10 ** 6
vBessel, vderBessel = Simpson(0, math.pi, 16, 0, 2 * math.pi, precision + 1)
sumBessel = [func + der for func, der in zip(vBessel, vderBessel)]
x = [i / precision * 2 * math.pi for i in range(precision + 1)]
plt.plot(x, vBessel, label="The Bessel func. J_1")
plt.plot(x, vderBessel, label="Der. of the Bessel func. J_0")
plt.ylim(-1, 1)
plt.xlim(0, 2 * math.pi)
plt.legend()
plt.show()
plt.plot(x, sumBessel, label="Sum of the func. and the der.")
plt.xlim(0, 2 * math.pi)
plt.legend()
plt.show()
