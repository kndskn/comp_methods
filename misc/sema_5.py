import matplotlib.pyplot as plt
import math as m


# functions
def interpolLagrange(x_k, y_k, n, t):
    P_n = 0
    for i in range(n + 1):
        numer = 1
        denomin = 1
        for j in range(n + 1):
            if i != j:
                numer *= t - x_k[j]
                denomin *= x_k[i] - x_k[j]
        P_n += y_k[i] * numer / denomin
    return P_n


# main body
n = int(input())
x_k = [(1 + k / n) for k in range(n + 1)]
y_k = [m.log(x) for x in x_k]
s = 10 ** 2
x = [0.5 + i / s * 2 for i in range(s + 1)]
Lagrange = [interpolLagrange(x_k, y_k, n, t) for t in x]
Ln = [m.log(t) for t in x]
plt.plot(x, Lagrange, 'r')
plt.plot(x_k, y_k, 'bo', markersize=4)
plt.ylim(-1 / 4, 1)
plt.xlim(1 / 2, 5 / 2)
plt.grid(True)
plt.legend()
plt.show()
