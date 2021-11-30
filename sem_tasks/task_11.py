import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy import sparse

N = 1000
Nit = 1000
Bound = pi
h = 2 * Bound / N
xspace_cont = np.linspace(-Bound, Bound, 10 ** 5)
xspace = np.linspace(-Bound, Bound, N)
accuracy = 1e-14


def U(arg):
    return (arg ** 2) / 2


def init_U_matrix():
    ans = np.diag(U(xspace))
    return ans


def matr_der_2():
    b = [0] + [-2 / h ** 2] * (N - 2) + [0]
    a = [1 / h ** 2] * (N - 2) + [0]
    c = [0] + [1 / h ** 2] * (N - 2)
    ans = sparse.diags([b, a, c], [0, -1, 1]).A
    return ans


def matrix(X_min, X_max):
    global x, A
    x = np.linspace(X_min, X_max, N)
    U_matr = init_U_matrix()
    der_2_matr = matr_der_2()
    A = -0.5 * der_2_matr + U_matr


def norm(f):
    return np.sqrt(np.trapz(f ** 2, dx=h))


def energy(f):
    return np.trapz(f * A.dot(f), dx=h)


def solve(psi0):
    end = 0
    psi = [psi0]
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(1, 1, 1)
    e = energy(psi[0])
    for i in range(1, Nit - 1):
        psi.append(np.linalg.solve(A, psi[i-1]))
        psi[i] = psi[i] / (norm(psi[i]))
        if abs(e - energy(psi[i])) > accuracy:
            e = energy(psi[i])
        else:
            e = energy(psi[i])
            end = i
            break
    # i = 1
    # psi.append(np.linalg.solve(A, psi[i - 1]))
    # psi[1] = psi[1] / (norm(psi[1]))
    # while abs(e - energy(psi[i - 1])) > accuracy:
    #     psi.append(np.linalg.solve(A, psi[i - 1]))
    #     psi[i] = psi[i] / (norm(psi[i]))
    #     e = energy(psi[i])
    #     end = i
    #     i += 1

    print(e)
    print(end)
    ax.plot(x, psi[end - 1] / norm(psi[end - 1]), label='psi')
    # plt.title('E=' + str(round(e, 3)))
    plt.plot(xspace_cont, np.exp(-0.5 * xspace_cont ** 2) * (np.pi) ** -0.25, label="Accurate solution")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    matrix(-Bound, Bound)
    z = np.linspace(-Bound, Bound, N)
    psi0 = z + z ** 2 + z ** 3
    solve(psi0)


if __name__ == '__main__':
    main()
