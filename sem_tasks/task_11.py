import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from tqdm import tqdm

INV = True
Bound = 10
N = 100
h = 2 * Bound / N
k = 100  # number of iteration
xspace = np.linspace(-Bound, Bound, N + 1)

def U(x):
    return 0.5 * x ** 2


def init_U_matrix():
    ans = np.diag(U(xspace))
    return ans


def matr_der_2():
    b = [0.] + [-2 / h ** 2] * (N - 1) + [0.]
    a = [1 / h ** 2] * (N - 1) + [0.]
    c = [0.] + [1 / h ** 2] * (N - 1)
    ans = sparse.diags([b, a, c], [0, -1, 1]).A
    return ans


def norm(f):
    return np.trapz(f ** 2) * h


def find_eig(psi_0, n_iter):
    psi = psi_0.copy()
    l = 0
    for i in range(n_iter):
        if INV:
            psi_it = A_inv.dot(psi).copy()
        else:
            psi_it = A.dot(psi).copy()
        if i == n_iter - 1:
            l = np.trapz(psi * A.dot(psi)) * h
        psi_it = psi_it / np.sqrt(norm(psi_it))
        psi = psi_it.copy()
    return psi, l


def update_Const(new_N, new_Bound):
    global N, h, xspace, psi_initial, der_2_matr, A, A_inv, U_matr
    N = new_N
    h = 2 * new_Bound / new_N
    xspace = np.linspace(-Bound, Bound, N + 1)
    psi_initial = (1 + xspace) * np.exp(-xspace ** 4)  # initial psi(x)
    U_matr = init_U_matrix()
    der_2_matr = matr_der_2()
    A = -0.5 * der_2_matr + U_matr
    A_inv = np.linalg.inv(-0.5 * der_2_matr + U_matr - 0 * np.eye(U_matr.shape[0]))


def main():
    update_Const(N, Bound)
    sol, lam = find_eig(psi_initial, k)
    plt.plot(xspace, sol, label="N = " + str(N))
    print("Energy of ground state E = ", lam)
    xspace_cont = np.linspace(-Bound, Bound, 10 ** 5)
    plt.plot(xspace_cont, np.exp(-0.5 * xspace_cont ** 2) * (np.pi) ** -0.25, label="Accurate solution")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
    # e = []
    # for i in range(100):
    #     e.append(abs(find_eig(psi_initial, i)[1] - 1.5))
    # xs = np.arange(100)
    # plt.plot(xs, e)
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()
