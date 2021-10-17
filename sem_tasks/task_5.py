import numpy as np
import matplotlib.pyplot as plt


def find_coeffs(x, y, c, n):
    f = np.zeros(n)
    for i in range(n):
        f[i] = y[i]
    c[0] = f[0]
    for i in range(1, n):
        for j in range(n - i):
            f[j] = (f[j + 1] - f[j]) / (x[j] - x[j])
        c[i] = f[0]  # Самый первый коэффициент, получившийся в новой итерации, является нашим очередным искомым к-том


def polynom(n, arg, x, c):
    temp = 0.
    result = 0.
    for k in range(n):
        temp = c[k]
        for i in range(k):
            temp *= (arg - x[i])
    result += temp
    return result


def main():
    m = 100
    n = 4
    x = np.zeros(n)
    y = np.zeros(n)
    c = np.zeros(n)
    arg = np.zeros(m)
    arg_pol = np.zeros(m)
    res = np.zeros(m)
    res_pol = np.zeros(m)
    for k in range(n):
        x[k] = 1 + k / n
        y[k] = np.log(x[k])
    find_coeffs(x, y, c, n)
    for k in range(n):
        res_pol[k] = polynom(n, 1 + k / 100, x, c)
        arg_pol[k] = 1 + k / 100
    for k in range(100):
        arg[k] = 0.5 + k / 50
        res[k] = polynom(n, 0.5 + k / 50, x, c - np.log(0.5 + k / 50))
    plt.plot(arg, res)
    plt.plot(arg_pol, res_pol)
    plt.show()


if __name__ == '__main__':
    main()
