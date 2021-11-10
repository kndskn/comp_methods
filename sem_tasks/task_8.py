import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


A = np.array([[998., 1998.], [-999., -1999.]])  # y' = Ay
y_0 = [1., 2.]
N = 1000
dh = 10 ** -4
tspace = np.linspace(0, N * dh, 1000)


def anal_sol(t, C1, C2):
    ans = []
    ans.append(-C1 * np.exp(-1000 * t) - 2 * C2 * np.exp(-t))
    ans.append(C1 * np.exp(-1000 * t) + C2 * np.exp(-t))
    return np.array(ans)


def Step(y):
    return A.dot(y)


def Euler(y_0, N_iter, dh):
    y = np.array(y_0)
    d = []
    d.append(y.copy())
    for i in tqdm(range(N_iter - 1)):
        y += Step(y) * dh
        d.append(y.copy())
    # print(d)
    return d


def Euler_implicit(y_0, N_iter_imp, N_iter_imp_newton, dh):
    y = np.array(y_0)
    d = []
    d.append(y.copy())
    y_i = y.copy()
    E = np.array([[1, 0], [0, 1]])
    for i in tqdm(range(N_iter_imp - 1)):
        y_i = y.copy()
        for j in range(N_iter_imp_newton):
            y += np.linalg.inv(E - dh * A).dot(y_i - y + dh * A.dot(y))
            d.append(y.copy())
    # print(d)
    return d


def main():
    for i in range(3):
        sol_dir = np.array(Euler(y_0, N // (10 ** i), dh * 10 ** i)).transpose()
        t_ax = (np.arange(N // (10 ** i)) * (10 ** i)) * dh
        plt.plot(t_ax, sol_dir[0], color='blue', label='direct, fact=' + str(10 ** i),
                 zorder=1)  # plotting of direct Euler
        sol_imp = np.array(Euler_implicit(y_0, N // (10 ** i), 3, dh * 10 ** i)).transpose()
        L = np.shape(sol_imp)[1]
        t_ax = (np.arange(L) * N / L) * dh
        plt.plot(t_ax, sol_imp[0], color='red', label='implicit, fact=' + str(10 ** i), zorder=1)
        plt.plot(tspace, anal_sol(tspace, 5, -3)[0], color='green', linestyle='--',
                 label='an_x, C1=1, C2=1', zorder=0)
        plt.ylim([0.9 * np.min(anal_sol(tspace, 5, -3)[0]), 1.1 * np.max(anal_sol(tspace, 5, -3)[0])])
        plt.legend()
        plt.show()
    # plt.plot(t_ax, sol[1], color = 'blue', label = 'y')


if __name__ == '__main__':
    main()
