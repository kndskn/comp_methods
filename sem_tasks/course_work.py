import numpy as np
import math as m
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft, fftfreq

lam = 2
c = 2
N = 1000
L = 10.0
x0 = -L
xN = L
h = (xN - x0) / N
Nt = 1000
t0 = 0
tN = 100
tau = (tN - t0) / Nt
t = [t for t in np.arange(t0, tN, tau)]
x = [x for x in np.arange(x0, xN, h)]


def a_t0(x):
    return c * lam / (m.cosh(lam * x))


def a_for_tm(a0, f, Nx, tj):
    f = a0 * np.exp(-2j * tau * (abs(f)) ** 2)
    f = fft(f, Nx)
    f = f * np.exp(-1j * tau * fftfreq(Nx, h) ** 2)
    f = np.abs(ifft(f, Nx))
    return f


def init_a():
    A = np.zeros((N, Nt))
    for i in range(N):
        A[i, 0] = a_t0(x[i])
    return A


def creation():
    b = init_a()
    for tj in range(1, Nt):
        psi = np.copy(b[:, tj - 1])
        psi_fin = a_for_tm(b[:, 0], psi, N, tj)
        b[:, tj] = psi_fin
    return b


if __name__ == '__main__':
    u = creation()
    u = np.transpose(u)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    X, T = np.meshgrid(x, t)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, T, u, rstride=1, cstride=1, cmap='viridis')
    ax.set_zlabel('A')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    plt.show()
