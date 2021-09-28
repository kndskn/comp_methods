import time
from math import *
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 / (np.tan((1 - x) ** 0.5)) - (1 / x - 1) ** 0.5


r = 1e-10
# b = max(1 - (pi*n)**2 - 0.1, 1)
# a = min(1 - (pi*(n+1))**2 + 0.9, 0.001)

b = 1 - 0.001
a = 0.001

x = np.linspace(a, b, 1000)
while (b - a) * 0.5 > r:
    if f(a) * f((a + b) * 0.5) <= 0:
        b = 0.5 * (a + b)
    #         print(f(a))
    else:
        a = 0.5 * (a + b)
#         print(f(a))
print('x =', a)
print('f(x) = ', f(a))
