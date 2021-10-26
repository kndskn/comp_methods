import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore

x_0 = 0
y_0 = 1
N = 100
right = 3
xspace = np.linspace(0, right, 1000)


def f(x, y):
    return -y


def euler(x_0, y_0, N_iter, right):
    y = y_0
    x = x_0
    dh = (right - x_0)/N_iter
    d = []
    for i in range(N_iter):
        y += f(x, y)*dh
        x += dh
        d.append([x, y])
    d = np.array(d)
    d = d.transpose()
    return y, x, d


def runge(x_0, y_0, N_iter, right):
    y = y_0
    x = x_0
    dh = (right - x_0)/N_iter
    d = []
    for i in range(N_iter):
        y += (0.25*f(x,y) + 0.75*f(x+2/3*dh, y + 2/3*dh*f(x, y)))*dh
        x += dh
        d.append([x, y])
    d = np.array(d)
    d = d.transpose()
    return y, x, d


def runge_upped(x_0, y_0, N_iter, right):
    y = y_0
    x = x_0
    dh = (right - x_0)/N_iter
    d = []
    for i in range(N_iter):
        k1 = f(x, y)
        k2 = f(x+dh/2, y + dh/2*k1)
        k3 = f(x+dh/2, y + dh/2*k2)
        k4 = f(x+dh, y + dh*k3)
        y += (k1 + 2*k2 + 2*k3 + k4)*dh/6
        x += dh
        d.append([x, y])
    d = np.array(d)
    d = d.transpose()
    return y, x, d


def main():
    for i in range(6, 15):
        N_inner = 2 ** i
        buf1, buf2, solve = euler(x_0, y_0, N_inner, right)
        if x_0 != 0:
            buf1, buf2, solve_2 = euler(x_0, y_0, N_inner, 0)
            solve = np.hstack((solve_2[:, ::-1], solve))
        diff = np.abs(solve[1] - y_0 * np.exp(-solve[0]) / np.exp(-x_0))
        plt.scatter(i, np.max(diff), c='red')
        print(Fore.RED + "Eu Maximum difference for N = " + str(2 ** i) + ", diff = ", np.max(diff))
        buf1, buf2, solve = runge(x_0, y_0, N_inner, right)
        if x_0 != 0:
            buf1, buf2, solve_2 = runge(x_0, y_0, N_inner, 0)
            solve = np.hstack((solve_2[:, ::-1], solve))
        diff = np.abs(solve[1] - y_0 * np.exp(-solve[0]) / np.exp(-x_0))
        plt.scatter(i, np.max(diff), c='green')
        print(Fore.GREEN + "2Ru Maximum difference for N = " + str(2 ** i) + ", diff = ", np.max(diff))
        buf1, buf2, solve = runge_upped(x_0, y_0, N_inner, right)
        if x_0 != 0:
            buf1, buf2, solve_2 = runge_upped(x_0, y_0, N_inner, 0)
            solve = np.hstack((solve_2[:, ::-1], solve))
        diff = np.abs(solve[1] - y_0 * np.exp(-solve[0]) / np.exp(-x_0))
        plt.scatter(i, np.max(diff), c='blue')
        print(Fore.BLUE + "4Ru Maximum difference for N = " + str(2 ** i) + ", diff = ", np.max(diff))
    plt.xlabel("2**i")
    plt.yscale('log')
    plt.grid()
    # plt.savefig('Ex_6.jpg')
    plt.show()


if __name__ == '__main__':
    main()
