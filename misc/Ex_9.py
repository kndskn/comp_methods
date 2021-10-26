import numpy as np
import matplotlib.pyplot as plt

N = 10
dh = np.pi/(N + 1)
A = [1/dh**2]*N
B = [-2/dh**2]*N
C = [1/dh**2]*N
D = np.sin(np.linspace(dh, np.pi - dh, N)).tolist()
BOUND_CONDITION = 3 # 0 - function at the bounds, 1 - derivative(left) and function(right) at the opposite bounds,
# 2 - derivative(right) and function(left) at the opposite bounds
# print(dh)
#bound cndition
# y(0) = a
ba = 1
#y(pi) = b
bb = 1
#y'(0) = c
bc = 0
#y'(pi) = d
bd = 10

def func_l(t):
    return 0

def func_r(t):
    return 0

def run_through(a, b, c, d):
    L = len(a)
    # a[0] = 0
    # c[L-1] = 0
    ans = [0]*L
    for i in range(1, L):
        ksi = a[i]/b[i-1]
        a[i] = 0
        b[i] = b[i] - ksi*c[i-1]
        d[i] = d[i] - ksi*d[i-1]
    ans[L-1] = (d[L-1]/b[L-1])
    for i in range(L-2, -1, -1):
        ans[i] = ((d[i] - c[i]*ans[i+1]) / b[i])
    return ans

def run_through_periodic(a,b,c,d):
    L = len(a)
    d_n = d[L-1]
    b_n = b[L-1]
    v, u_minus = [0]*(L-2), [0]*(L-2)
    v[0], u_minus[0] = c[L-1], -a[0]
    u_minus.append(-c[L-2])
    v.append(c[L-1])
    p = run_through(a[:-1], b[:-1], c[:-1], d[:-1])
    q = run_through(a[:-1], b[:-1], c[:-1], u_minus[:])
    ans = [0]*L
    ans[L-1] = (d[L-1] - c[L-1]*p[0] - a[L-1]*p[L-2])/(b_n + c[L-1]*q[0] + a[L-1]*q[L-2])
    x_n = ans[L-1]
    for i in range(L-2, -1, -1):
        ans[i] = p[i] + x_n*q[i]
    return ans


# boundary conditions y(0) = y(pi) = 0 -> solution y(x) = - sin(x)
# if y(0) = y(pi) and y'(0) = y'(pi) doesn't have any solutions
if BOUND_CONDITION == 0:
    A[0] = 0
elif BOUND_CONDITION == 1:
    A[0] = 0
    B[0] = -1/dh**2
elif BOUND_CONDITION == 2:
    A[0] = 0
    B[N-1] = -1/dh**2
elif BOUND_CONDITION == 3:
    A[0] = 0
    B[0] = -1/dh**2
elif BOUND_CONDITION == 4:
    A[0] = 0
    B[N-1] = -1/dh**2
xspace = np.linspace(0, np.pi, N+2)
xspace_cont = np.linspace(0, np.pi, 10000)
# print(run_through(A,B,C,D))
sol = run_through(A, B, C, D)
if BOUND_CONDITION == 0:
    sol = [0] + sol + [0]
    sol = sol - ba*(xspace - np.pi)/np.pi + bb*xspace/np.pi
    c1 = ba
    c2 = (bb - ba) / np.pi
elif BOUND_CONDITION == 1:
    sol = [sol[0]] + sol + [0]
    sol = sol + bc * (xspace - np.pi) + bb
    c1 = bb - (bc+1)*np.pi
    c2 = bc + 1
elif BOUND_CONDITION == 2:
    sol = [0] + sol + [sol[-1]]
    sol = sol + bd * xspace + ba
    c1 = ba
    c2 = bd - 1
elif BOUND_CONDITION == 3:
    sol = [sol[0]] + sol +[0]
    sol = sol + bc * xspace + ba - sol[0]
    c1 = ba
    c2 = bc + 1
elif BOUND_CONDITION == 4:
    sol = [0] + sol +[sol[-1]]
    sol = sol + bd * (xspace - np.pi) + bb - sol[-1]
    c1 = bb - (bc-1)*np.pi
    c2 = bd - 1
plt.plot(np.linspace(0, np.pi, N+2), sol)
# solution y = -sin(x) + c1*x + c2
# y(0) = a
# y(pi) = (b-a+sin(L))/L
plt.plot(xspace_cont, -np.sin(xspace_cont) + c2*xspace_cont + c1)
plt.xlim([0, np.pi])
# plt.ylim([-1.1, 0])
plt.grid()
plt.show()

