import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 2
c = 2
d = 10
y_0 = [6, 6]
N = 10000
dh = 10 ** -2
count = 0
accuracy = 10 ** -5
N_implicit = 100
N_plots = 1


def solution(y):
    return 5 * np.log(y[0] * y[1] / y_0[0] / y_0[1]) - (y[1] + y[0]) + (y_0[0] + y_0[1])  # analitical solution


def Step(vec):
    ans = []
    ans.append(a * vec[0] - b * vec[1] * vec[0])
    ans.append(- d * vec[1] + c * vec[1] * vec[0])
    ans = np.array(ans)
    return ans


def Runge(y_0, N_iter, dh):
    y = y_0
    d = []
    d2 = []
    d1 = []
    d3 = []
    for i in range(N_iter):
        y += (0.25 * Step(y) + 0.75 * Step(y + 2 / 3 * dh * Step(y))) * dh
        d.append(y.copy())
        d2.append(y[0] + y[1])
        d1.append(y[0])
        d3.append(y[1])
    # plt.plot(np.arange(1, N_iter + 1), d2, label="foxes and rabbits")
    plt.plot(np.arange(1, N_iter + 1), d1, label="rabbits")
    plt.plot(np.arange(1, N_iter + 1), d3, label='foxes')
    plt.grid()
    plt.xlim([0, N])
    plt.legend()
    plt.show()
    d = np.array(d)
    d = d.transpose()
    # print(d[0], d[1])
    # plt.plot(d[0], d[1] - np.exp(-d[0]))
    # plt.plot(xspace, np.exp(-xspace))
    return y, d, d1, d3


def Euler(y_0, N_iter, dh):
    y = y_0
    vec = y / np.linalg.norm(y)
    dh_vec = dh * vec
    d = []
    for i in range(N_iter):
        y += Step(y) * dh_vec
        vec = y / np.linalg.norm(y)
        dh_vec = dh * vec
        d.append(y.copy())
    d = np.array(d)
    d = d.transpose()
    return y, d


def main():
    for i in range(N_plots):
        y_0_in = [y_0[0] + i / N_plots, y_0[1]]
        print(solution(y_0_in))
        buf, sol, rab, fox = Runge(y_0_in, N, dh)
        plt.plot(sol[0], sol[1], color='blue')
        # buf, sol = Euler(y_0_in, N, dh)
        # plt.plot(sol[0], sol[1], color = 'green')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
