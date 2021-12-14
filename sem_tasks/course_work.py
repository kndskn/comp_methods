import numpy as np
import math as m
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft, fftfreq

lam = 2
c = 100
delta = 0
L = 10.0
x_1 = -L + delta
x_N = L - delta
t_1 = 0.0
t_N = 1
N = 1000
h = (x_N - x_1) / N
Nt = 1000
tau = (t_N - t_1) / Nt
t = [t for t in np.arange(t_1, t_N, tau)]
x = [x for x in np.arange(x_1, x_N, h)]


def a_for_t0(x):
    return c * lam / (m.cosh(lam * x))


a0 = [a_for_t0(x) for x in np.arange(x_1, x_N, h)]
a = [a0]


def a_for_tm(a, N):
    a = np.array(a)
    f = [0.0] * (N)
    f = np.array(f)
    f = a * np.exp(-2j * (abs(a)) ** 2 * tau)
    f = fft(f, N, axis=-1)
    f = f * np.exp(1j * 5 * tau * fftfreq(N, 1 / (m.pi * 100)) ** 2)
    f = ifft(f, N, axis=-1)
    return f


p = 0
while p < (len(t) - 1):
    c = a_for_tm(a[p], N)
    c = list(c)
    a.append(c)
    p += 1

A_2D = np.array(a)
A_1D = A_2D.flatten()
X, T = np.meshgrid(x, t)
A = np.reshape(A_1D, T.shape)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(T, X, A)
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('A')
plt.show()

a1 = np.conj(a)
f = np.multiply(a, a1)
f = f.transpose()
z = sum(f)
