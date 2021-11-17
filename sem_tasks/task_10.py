import numpy as np
import matplotlib.pyplot as plt

L = 1
N = 10
Nt = 100
dt = 1e-2
h = L/N
T = Nt*dt
SHOW_EVOL = True
SHOW_MAX_T = True


def f_init(x):
    return x*(1-x/L)**2


def diff_operator(in_v):
    ans_v = [0]*(len(in_v))
    ans_v[0] = 0
    ans_v[len(in_v)-1] = 0
    for i in range(1, len(in_v) - 1):
        ans_v[i] = (in_v[i+1] - 2*in_v[i] + in_v[i-1])/h**2
    return ans_v


def run_through(a, b, c, d):
    L = len(a)
    a[0] = 0
    c[L-1] = 0
    ans = [0]*L
    for i in range(1, L):
        ksi = a[i]/b[i-1]
        a[i] = 0
        b[i] = b[i] - ksi*c[i-1]
        d[i] = d[i] - ksi*d[i-1]
    ans[L-1] = (d[L-1]/b[L-1])
    for i in range(L-2, -1, -1):
        ans[i] = ((d[i] - c[i]*ans[i+1]) / b[i])
    return ans


def main():
    # initial V
    v_0 = []
    for i in range(N + 1):
        v_0.append(f_init(i * h))
    # print(v_0)

    # use only 1..N-1 elements

    A = [-0.5 * dt / h ** 2] * (N)
    A[1] = 0
    B = [1 + dt / h ** 2] * (N)
    C = [-0.5 * dt / h ** 2] * (N)
    C[N - 1] = 0
    D = [0] * N
    buf_v = diff_operator(v_0)
    for i in range(N):
        D[i] = v_0[i] + dt / 2 * buf_v[i]

    xspace = np.linspace(0, L, len(v_0))
    plt.plot(xspace, v_0)
    T_max = [max(v_0)]
    for i in range(Nt):
        v = run_through(A[1:], B[1:], C[1:], D[1:])
        v = [0] + v + [0]
        buf_v = diff_operator(v)
        for i in range(N):
            D[i] = v[i] + dt / 2 * buf_v[i]
        xspace = np.linspace(0, L, len(v))
        plt.plot(xspace, v)
        T_max.append(max(v))
    plt.xlim([0, L])
    plt.grid()
    if SHOW_EVOL:
        plt.show()
    else:
        plt.close()
    tspace = np.linspace(0, T, Nt + 1)
    plt.plot(tspace, T_max)
    plt.xlim([0 - T * 0.05, T * 1.05])
    plt.grid()
    if SHOW_MAX_T:
        plt.show()
    else:
        plt.close()


if __name__ == '__main__':
    main()
