import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style

#Euler method 1st order of accuracy

x_0 = 2.5
y_0 = 1
N = 100
right = 5
xspace = np.linspace(0, right, 1000)


def Eu_step(x, y):
    return -y


def Euler(x_0, y_0, N_iter, right):
    y = y_0
    x = x_0
    dh = (right - x_0)/N_iter
    d = []
    for i in range(N_iter):
        y += Eu_step(x, y)*dh
        x += dh
        d.append([x, y])
    d = np.array(d)
    d = d.transpose()
    return (y, x, d)

#Runge method 2nd order of accuracy

def Runge(x_0, y_0, N_iter, right):
    y = y_0
    x = x_0
    dh = (right - x_0)/N_iter
    d = []
    for i in range(N_iter):
        y += (0.25*Eu_step(x,y) + 0.75*Eu_step(x+2/3*dh, y + 2/3*dh*Eu_step(x, y)))*dh
        x += dh
        d.append([x, y])
    d = np.array(d)
    d = d.transpose()
    # print(d[0], d[1])
    #plt.plot(d[0], d[1] - np.exp(-d[0]))
    # plt.plot(xspace, np.exp(-xspace))
    return (y, x, d)

#Runge method 4nd order of accuracy

def Runge_upped(x_0, y_0, N_iter, right):
    y = y_0
    x = x_0
    dh = (right - x_0)/N_iter
    d = []
    for i in range(N_iter):
        k1 = Eu_step(x, y)
        k2 = Eu_step(x+dh/2, y + dh/2*k1)
        k3 = Eu_step(x+dh/2, y + dh/2*k2)
        k4 = Eu_step(x+dh, y + dh*k3)
        y += (k1 + 2*k2 + 2*k3 + k4)*dh/6
        x += dh
        d.append([x, y])
    d = np.array(d)
    d = d.transpose()
    # print(d[0], d[1])
    #plt.plot(d[0], d[1] - np.exp(-d[0]))
    # plt.plot(xspace, np.exp(-xspace))
    return (y, x, d)


for i in range(6,15):
    N_inner = 2**i
    buf1, buf2, solve = Euler(x_0, y_0, N_inner, right)
    if x_0 != 0:
        buf1, buf2, solve_2 = Euler(x_0, y_0, N_inner, 0)
        solve = np.hstack((solve_2[:,::-1],solve))
    diff = np.abs(solve[1] - y_0*np.exp(-solve[0])/np.exp(-x_0))
    plt.scatter(i, np.max(diff), c = 'red')
    print(Fore.RED + "Eu Maximum difference for N = "+str(2**i) + ", diff = ", np.max(diff))
    buf1, buf2, solve = Runge(x_0, y_0, N_inner, right)
    if x_0 != 0:
        buf1, buf2, solve_2 = Runge(x_0, y_0, N_inner, 0)
        solve = np.hstack((solve_2[:,::-1],solve))
    diff = np.abs(solve[1] - y_0*np.exp(-solve[0])/np.exp(-x_0))
    plt.scatter(i, np.max(diff), c = 'green')
    print(Fore.GREEN + "2Ru Maximum difference for N = "+str(2**i) + ", diff = ", np.max(diff))
    buf1, buf2, solve = Runge_upped(x_0, y_0, N_inner, right)
    if x_0 != 0:
        buf1, buf2, solve_2 = Runge_upped(x_0, y_0, N_inner, 0)
        solve = np.hstack((solve_2[:,::-1],solve))
    diff = np.abs(solve[1] - y_0*np.exp(-solve[0])/np.exp(-x_0))
    plt.scatter(i, np.max(diff), c = 'blue')
    print(Fore.BLUE + "4Ru Maximum difference for N = "+str(2**i) + ", diff = ", np.max(diff))
plt.xlabel("2**i")
plt.yscale('log')
plt.grid()
plt.savefig('Ex_6.jpg')
plt.show()