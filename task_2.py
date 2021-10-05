import numpy as np
import matplotlib.pyplot as plt

# Some parameters

a0 = 1.  # the width of the potential pit
U0 = 5.  # the depth of the potential pit
A = 2. * (a0 ** 2.) * U0
accuracy = 1e-15  # calculation accuracy
n_max = A / np.pi  # maximum energy level


def find_epsilon():
    eps = 1.
    i = 0
    x1 = 0.
    while 1.0 != 1.0 + eps:
        eps /= 2
    return eps


def find_max_energy_level():
    eps = find_epsilon()
    print("Maximum energy level:", int(n_max) - 1,
          "\nEnter required energy level, less then maximum:\n")
    n = int(input())
    l = 1 - np.pi ** 2 * (n + 1) ** 2 / (A ** 2) + eps
    r = 1 - np.pi ** 2 * n ** 2 / (A ** 2) - eps
    return l, r


def f(x):
    """Resulted function from definition of
    Schrodinger equation for potential pit"""
    return ((np.tan(A * (1 - x) ** (1 / 2))) ** (-1)) - ((1 / x) - 1) ** (1 / 2)


def df(x):
    """The derivative of the function f(x)"""
    return A / (2 * (1 - x) ** (1 / 2) * (np.sin(A * (1 - x) ** (1 / 2))) ** 2) \
           + 1 / (2 * x ** 2 * (1 / x - 1) ** (1 / 2))


def dichotomy(l, r):
    """ This method contains the implementation of finding
    the zero of a function by the dichotomy method """
    while (r - l) * 0.5 > accuracy:
        if f(l) * f((l + r) * 0.5) <= 0:
            r = (r + l) * 0.5
        else:
            l = (r + l) * 0.5
    print('Results of Dihotomy method:',
          '\n-E_0/U =', l, '\n{DEBUG DICHOTOMY}', '\nf(x) = ', f(l), '\n')


def simple_iterations(l, r):
    """ This method contains the implementation of finding
     the zero of a function by the simple iteration method """
    x = (r + l) * 0.5
    while True:
        lya = 1 / df(x)
        phi = x - lya * f(x)
        x1 = phi
        if abs(x - x1) < accuracy:
            break
        x = x1
        # print('f(x) = ', f(x), '\nx = ', x, '\n')
    print('Results of simple iterations method:', '\n-E_0/U =',
          x1, '\n{DEBUG SIMPLE ITERATION}', '\nf(x) = ', f(x1), '\n')


def newton_method(l, r):
    """ This method contains the implementation of finding
     the zero of a function by the Newton's method """

    i = 0
    x1 = 0.
    x = r
    while x > l:
        i += 1
        x1 = x
        x = x1 - f(x1) / (df(x1))
        if abs(x - x1) < accuracy and abs(f(x)) < 1e-5:
            break
    # print(i) # Print number of iterations
    # print(l, r) # Print segment ends
    print('Results of Newton method:', '\n-E_0/U =',
          x1, '\n{DEBUG NEWTON}', '\nf(x) = ', f(x1), '\n')


def secant(l, r):
    """ This method contains the implementation of finding
    the zero of a function by the secant method """
    i = 0
    dx = (r - l) / 1000
    x = r
    while True:
        i += 1
        x1 = x
        if (x1 + dx) > r:
            x = x1 - f(x1) * dx / (f(x1) - f(x1 - dx))
        else:
            x = x1 - f(x1) * 2 * dx / (f(x1 + dx) - f(x1 - dx))
        if abs(x - x1) < accuracy:
            break
    # print(i) # Print number of iterations
    # print(l, r) # Print segment ends
    print('Results of secant method:', '\n-E_0/U =',
          x1, '\n{DEBUG SECANT}', '\nf(x) = ', f(x1), '\n')


def draw(a, b):
    """ This method contains the implementation of
    drawing graph of function """

    x = np.linspace(a, b, 1000)
    plt.plot(x, f(x))
    plt.ylim([-3, 3])
    plt.show()


def main():
    l, r = find_max_energy_level()
    dichotomy(l, r)
    simple_iterations(l, r)
    newton_method(l, r)
    secant(l, r)


if __name__ == '__main__':
    main()
