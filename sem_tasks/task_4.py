from math import *


def f(m, x, t): return cos(m * t - x * sin(t))


def bessel(x, m):
    """ Simpson integral calculation """
    temp = 0.
    dt = pi / 100.
    for i in range(1, 100):
        temp += (dt / 6) * (f(m, x, (i - 1) * dt) + 4 * f(m, x, (2 * i - 1) * dt / 2) + f(m, x, i * dt))
    return temp / pi


def main():
    i, n = 100., 100.
    dx = 2 * pi / n
    delta_x = 1e-10
    for i in range(0, int(n)):
        j0_der = (bessel(0, i * dx + delta_x) - bessel(0, i * dx - delta_x)) / (2 * delta_x)
        print(abs(j0_der + bessel(1, i * dx)))


if __name__ == '__main__':
    main()
