import numpy as np
import matplotlib.pyplot as plt

# Some parameters

m = 1.  # mass (from Schrodinger equation)
a0 = 1.  # the width of the potential pit
U0 = 5.  # the depth of the potential pit
A = 2. * (a0 ** 2.) * U0
accuracy = 1e-5  # calculation accuracy
a = 0 + 1e-10
b = 1 - 1e-10


def f(x):
    """Resulted function from definition of
    Schrodinger equation for potential pit"""
    return ((np.tan(A * (1 - x) ** (1 / 2))) ** (-1)) - ((1 / x) - 1) ** (1 / 2)


def df(x):
    """The derivative of the function f(x)"""
    return A / (2 * (1 - x) ** (1 / 2) * (np.sin(A * (1 - x) ** (1 / 2))) ** 2) \
           + 1 / (2 * x ** 2 * (1 / x - 1) ** (1 / 2))


def dichotomy(a, b):
    """ This method contains the implementation of finding
    the zero of a function by the dichotomy method """

    while (b - a) * 0.5 > accuracy:
        if f(a) * f((a + b) * 0.5) <= 0:
            b = (b + a) * 0.5
        else:
            a = (b + a) * 0.5
    print('Results of Dihotomy method:',
          '\n-E_0/U =', a, '\n\n\n{DEBUG}', '\nf(x) = ', f(a), '\n')


def simple_iterations():
    """ This method contains the implementation of finding
    the zero of a function by the simple iterations method """

    print()


def newton_method(A):
    """ This method contains the implementation of finding
     the zero of a function by the Newton's method """

    eps = 1.
    i = 0
    x1 = 0.
    while 1.0 != 1.0 + eps:
        eps /= 2
    n_max = A / np.pi
    print("Maximum energy level:", int(n_max) - 1,
          "\nEnter required energy level, less then maximum:\n")
    n = int(input())
    if n > n_max:
        print("Enter level less maximum:\n")
        n = int(input())
        l = 1 - np.pi ** 2 * (n + 1) ** 2 / (A ** 2) + eps
        r = 1 - np.pi ** 2 * n ** 2 / (A ** 2) - eps
    else:
        l = 1 - np.pi ** 2 * (n + 1) ** 2 / (A ** 2) + eps
        r = 1 - np.pi ** 2 * n ** 2 / (A ** 2) - eps
    x = r
    while x > l:
        i += 1
        x1 = x
        x = x1 - f(x1) / (df(x1))
        if abs(x - x1) < 1e-10 and abs(f(x)) < 1e-5:
            break
    # print(i) # Print number of iterations
    # print(l, r) # Print segment ends
    print('Results of Newton method:', '\n-E_0/U =',
          x1, '\n\n\n{DEBUG}', '\nf(x) = ', f(x1), '\n')


def draw(a, b):
    """ This method contains the implementation of
    drawing graph of function """

    x = np.linspace(a, b, 1000)
    plt.plot(x, f(x))
    plt.ylim([-3, 3])
    plt.show()


def main():
    dichotomy(a, b)
    newton_method(A)


if __name__ == '__main__':
    main()
