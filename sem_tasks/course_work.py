import numpy as np
import math as m
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft, fftfreq
from task_12 import Fourier_matrix_dir, Fourier_matrix_rev

lam = 2
c = 1
N = 100
L = 10.0
x0 = -L
xN = L
h = (xN - x0) / N
Nt = 1000
t0 = 0
tN = 20
tau = (tN - t0) / Nt
t = [t for t in np.arange(t0, tN, tau)]
x = [x for x in np.arange(x0, xN, h)]


def a_t0(x):
    return c * lam / (m.cosh(-lam * x))


# def a_for_tm(f0, f, Nx):
#     f = f * np.exp(-2j * tau * 0 * (abs(f)) ** 2)
#     c = abs(fft(f, Nx))
#     f = fft(f, Nx)
#     f = f * np.exp(-1j * tau * fftfreq(Nx, h) ** 2)
#     f = np.abs(ifft(f, Nx))
#     return f, c


def a_for_tm(f0, f, Nx):
    F_dir = Fourier_matrix_dir(Nx)
    F_rev = Fourier_matrix_rev(Nx)
    f = f0 * np.exp(-2j * tau * (abs(f)) ** 2)
    image = F_dir.dot(f)
    c = abs(image)
    f = image
    f = f * np.exp(-1j * tau * fftfreq(Nx, h) ** 2)
    re_func = np.real(F_rev.dot(f))
    f = np.abs(re_func)
    return f, c


def init_a(Nx, N_t):
    A = np.zeros((Nx, N_t))
    fA = np.zeros((Nx, N_t))
    for i in range(Nx):
        A[i, 0] = a_t0(x[i])
    fA[:, 0] = abs(fft(A[:, 0], Nx))
    return A, fA


def creation(Nx, N_t):
    b, fA = init_a(Nx, N_t)
    for tj in range(1, N_t):
        psi = np.copy(b[:, tj - 1])
        psi_fin, psi_fA = a_for_tm(b[:, 0], psi, Nx)
        b[:, tj] = psi_fin
        fA[:, tj] = psi_fA
    return b, fA


def show_check(f, Nx, N_t, step):
    buf = np.copy(f)
    for tj in range(1, N_t):
        if (tj % step) == 0:
            c = np.roll(buf[:, tj], N // 2)
            wspace = np.roll(fftfreq(Nx, h), N // 2)
            plt.plot(wspace, c, label='time step ' + str(tj))
            plt.xlabel("k")
            plt.ylabel("|A(k)|")
            plt.title("Checking the nonlinear step")
            plt.legend()
            plt.show()
    return 0


def show_abs_A_x(f, Nx, N_t, step):
    buf = np.copy(f)
    for tj in range(1, N_t):
        if (tj % step) == 0:
            plt.plot(x, buf[:, tj], label='time step ' + str(tj), color='red')
            plt.xlabel("x")
            plt.ylabel("|A(x)|")
            plt.title("Checking the signal")
            plt.legend()
            plt.show()
    return 0


def im_make(f):
    u = np.transpose(f)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    X, T = np.meshgrid(x, t)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, T, u, rstride=1, cstride=1, cmap='viridis')
    ax.set_zlabel('|A(x,t)|')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.view_init(20, 50)
    plt.show()
    return


if __name__ == '__main__':
    u, check = creation(N, Nt)
    print('1 - |A(k)| in real time\n2 - |A(x)| in real time\n3 - 3D surface |A(x,t)| \n')
    temp = int(input())
    if temp == 1:
        show_check(check, N, Nt, 50)
    elif temp == 2:
        show_abs_A_x(u, N, Nt, 5)
    elif temp == 3:
        im_make(u)
