import numpy as np
import matplotlib.pyplot as plt

m = 1.
a0 = 1.
U0 = 10.
n = 0
accuracy = 1e-10
a = 0 + 1e-10
b = 1 - 1e-10


def f(x):
    return 1 / (np.tan((2 * (a0 ** 2) * U0 * (1 - x)) ** (1 / 2))) - (1 / x - 1) ** 0.5


def dihotomy(a, b):
    while (b - a) * 0.5 > accuracy:
        if f(a) * f((a + b) * 0.5) <= 0:
            b = (b + a) * 0.5
        else:
            a = (b + a) * 0.5
    print('x =', a)
    print('f(x) = ', f(a))


def draw(a, b):
    x = np.linspace(a, b, 1000)
    plt.plot(x, f(x))
    plt.ylim([-3, 3])
    plt.show()


def main():
    dihotomy(a, b)


if __name__ == '__main__':
    main()
