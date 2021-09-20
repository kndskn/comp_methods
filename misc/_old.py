
from math import *
import numpy as np


def f(x):
    return tan(x) - x


def df(x):
    return (cos(x)) ** (-2) - 1


def ddf(x):
    return 2 * sin(x) / (cos(x)) ** 3


accuracy = 1e-10
num = -log10(accuracy)
print(num)

# dihotomy

nd = 2
a = -pi / 2. + 0.000001 + pi * (nd - 1)
b = pi / 2. - 0.000001 + pi * (nd - 1)
# kd = 10
kd = int(log2(pi / accuracy) + log2(10))

for i in range(1, kd):
    if (f((b + a) * 0.5) * f(a)) <= 0:
        b = (b + a) * 0.5
    else:
        a = (b + a) * 0.5

# p1 = str((b+a)/2)

# s = '.' + str(int(num)) + 'f'

# format(p1, s)

# print (pl)

print('dihotomy ', (b + a) / 2, ' ', kd)

# simple iterations

ns = nd
x = [(ns - 1) * pi / 2]
ks = int(log(ns * pi / accuracy) / log(((ns - 1) * pi / 2 + pi / 4) ** 2 + 1)) + 1

for i in range(1, ks):
    x.append(atan(x[i - 1]) + (ns - 1) * pi)

# print(log(ns*pi/accuracy),log(((ns-1)*pi/2+pi/4)**2+1))

print('iterations', x[ks - 1], ' ', ks)

# newton

n = nd
y = [-1 / (pi / 2 + pi * (n - 1)) + pi / 2 + pi * (n - 1)]
k = int(sqrt(-log10(accuracy)))
# alpha = 0.5*ddf(y[0])/df(y[0])
# k = int(log2(log(alpha*accuracy)/log(alpha*(1/(pi/2+pi*(n-1))))))
# for i in range(0, k):
#     y.append(y[i - 1] - f(y[i - 1]) / df(y[i - 1]))
#     print('newton ', y[k - 1], ' ', k)

# if __name__ == '__main__':
#     main()
