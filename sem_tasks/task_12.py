import numpy as np
import matplotlib.pyplot as plt

rec = True
im= True
N = 1000
T = 2*np.pi
a0, a1 = 10, 0.002
w0, w1 = 5.1, 25.5
xspace = np.linspace(-T/2, T/2, N)


def func(x):
    return a0*np.sin(2*np.pi*w0*x) + a1*np.sin(2*np.pi*w1*x)


def H_window(y, x):
    return 0.5*(1 + np.cos(x))*y


def re_H_window(y, x):
    div = 1 + np.cos(x)
    div[div == 0] = 2e-16
    return y/(0.5*div)


def Fourier_matrix_dir(n):
    row = np.arange(0, n, 1)
    i = 1j
    row = np.exp(2*np.pi*i*row/n)
    matr = np.array([row**i for i in range(n)])
    C_plus = 1/n
    return C_plus*matr


def Fourier_matrix_rev(n):
    row = np.arange(0, n, 1)
    i = 1j
    row = np.exp(-2*np.pi*i*row/n)
    matr = np.array([row**i for i in range(n)])
    return matr


def main():
    F_dir = Fourier_matrix_dir(N)
    F_rev = Fourier_matrix_rev(N)
    image = F_dir.dot(func(xspace))
    image_H = F_dir.dot(H_window(func(xspace), xspace))
    if im:
        wspace = np.arange(0, N, 1) / T  # - (N-1)/2/T)
        plt.plot(wspace, 2 * np.abs(image), label='rect')
        plt.plot(wspace, 2 * np.abs(image_H), label='Hann')
        plt.xlim([0, np.max(wspace) / 2])
        plt.yscale('log')
        plt.legend()
        plt.show()

    if rec:
        re_func = np.real(F_rev.dot(image))
        re_func_H = re_H_window(np.real(F_rev.dot(image_H)), xspace)
        print("STD for rectangle window s =", np.std(re_func - func(xspace)))
        print("STD for Hann window s =", np.std(re_func_H[1:-1] - func(xspace)[1:-1]))
        plt.plot(xspace, np.abs(re_func - func(xspace)), label='rect')
        plt.plot(xspace, np.abs(re_func_H - func(xspace)), label='Hann')
        plt.yscale('log')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()
