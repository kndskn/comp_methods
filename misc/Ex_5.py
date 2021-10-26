import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

add_px = 1.1
add_py = 1


def diff(n, y, x, ind):
    if n == 1:
        return y[ind[0]]
    return (diff(n-1, y, x, ind[:-1]) - diff(n-1, y, x, ind[1:]))/(x[ind[0]] - x[ind[-1]])

def mult(k, X, x):
    ans = 1
    for i in range(k):
        ans *= x-X[i]
    return ans

def P(Y, X, x):
    ans = Y[0]
    N = len(Y)
    for i in range(2, N+1):
        ans += diff(i, Y, X, range(i))*mult(i-1, X, x)
    return ans

def trans(X):
    inner_x = np.array(X)
    inner_x = inner_x.transpose()
    ans = inner_x.tolist()
    return ans

xspace = np.linspace(1,2,500)
for n in range(3,10,3):
    XY = []
    for k in range(n+1):
        XY.append([1 + k/n, np.log(1 + k/n)])
    XY = sorted(XY, key=lambda x: x[0])
    XY = trans(XY)
    X_without, Y_without = XY[0], XY[1]
    XY = trans(XY)
    Y_ip_without = np.array(P(Y_without, X_without, xspace))
    X_without = np.array(X_without)
    Y_without = np.array(Y_without)

    if not add_px in XY[0]:
        XY.append([add_px, add_py])
    else:
        print("You chose bad point")
    # print(XY)
        # sorting of a an array
    XY = sorted(XY, key=lambda x: x[0])
    # print(XY)
    XY = trans(XY)
    # print(XY)
    X_with, Y_with = XY[0], XY[1]
    # Y_arr = np.abs(np.array(P(Y, X, xspace)) - np.log(xspace))
    # X = np.array(X)
    # Y = np.abs(np.array(Y) - np.log(X))
    Y_ip_with = np.array(P(Y_with, X_with, xspace))
    X_with = np.array(X_with)
    Y_with = np.array(Y_with)

    #plotting
    fig, axes = plt.subplots(1,1, figsize = (13,6))
    axes.plot(xspace, Y_ip_with, color = 'red') # with new point
    axes.plot(xspace, Y_ip_without, color = 'red', linestyle = '--') # with new point
    axes.scatter(X_without, Y_without)
    # axes[1].plot(xspace, Y_ip_without, color = 'red') # with new point
    # axes[1].scatter(X_without, Y_without)
    axes.scatter(add_px, add_py, c = 'blue')
    plt.title('n = ' + str(n))
    #plt.xlim([1,2])
    # plt.yscale('log')
    axes.grid()
    # axes[1].grid()
    plt.show()
#plt.yscale('log')
#plt.show()

