from math import *
import numpy as np

m = 1
a0 = 1
U0 = 1
h = 1


def f(x):
    return 1 / (tan(sqrt(2 * m * a0 ** 2 * U0 / (h ** 2) * (1 - (-x / U0))))) - sqrt(1 / (-x / U0) - 1)


# def df(x):
#     return (cos(x)) ** (-2) - 1
#
#
# def ddf(x):
#     return 2 * sin(x) / (cos(x)) ** 3

accuracy = 1e-10
num = -log10(accuracy)
nd = 2
# kd = 10
kd = int(log2(pi / accuracy) + log2(10))


def dihotomy():
    a = -pi / 2. + 0.000001 + pi * (nd - 1)
    b = pi / 2. - 0.000001 + pi * (nd - 1)
    for i in range(1, kd):
        if (f((b + a) * 0.5) * f(a)) <= 0:
            b = (b + a) * 0.5
        else:
            a = (b + a) * 0.5


def main():
    dihotomy()


if __name__ == '__main__':
    main()
