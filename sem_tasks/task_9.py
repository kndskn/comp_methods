import numpy as np
import matplotlib.pyplot as plt

# Boundary conditions left:  c_1 * y + c_2 * y' = u_0
# Boundary conditions right:  c_3 * y + c_4 * y' = u_1

c_1 = 1
c_2 = 0
c_3 = 1
c_4 = 0
u_0 = 0
u_1 = 0
N = 100

dh = np.pi / (N + 1)
A = [1 / dh ** 2] * N
B = [-2 / dh ** 2] * N
C = [1 / dh ** 2] * N
D = np.sin(np.linspace(dh, np.pi - dh, N)).tolist()

D[0] -= (u_0 * dh) / (- c_2 + c_1 * dh) / dh ** 2
B[0] += - c_2 / (- c_2 + c_1 * dh) / dh ** 2
D[N - 1] -= (u_1 * dh) / (c_4 + c_3 * dh) / dh ** 2
B[N - 1] += c_4 / (c_4 + c_3 * dh) / dh ** 2


def func_l(t):
    return 0


def func_r(t):
    return 0


def run_through(a, b, c, d):
    L = len(a)
    ans = [0] * L
    for i in range(1, L):
        ksi = a[i] / b[i - 1]
        a[i] = 0
        b[i] = b[i] - ksi * c[i - 1]
        d[i] = d[i] - ksi * d[i - 1]
    ans[L - 1] = (d[L - 1] / b[L - 1])
    for i in range(L - 2, -1, -1):
        ans[i] = ((d[i] - c[i] * ans[i + 1]) / b[i])
    return ans


def main():
    xspace = np.linspace(0, np.pi, N + 2)
    sol = run_through(A, B, C, D)
    y0 = (u_0 * dh - c_2 * sol[0]) / (- c_2 + c_1 * dh)
    yN = (u_0 * dh + c_4 * sol[N - 1]) / (c_4 + c_3 * dh)
    sol = [y0] + sol + [yN]
    plt.plot(xspace, sol)
    c1 = 0
    c2 = 0
    xspace_cont = np.linspace(0, np.pi, 10000)
    plt.plot(xspace_cont, -np.sin(xspace_cont) + c2 * xspace_cont + c1)
    plt.xlim([0, np.pi])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
