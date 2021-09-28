import math as m

a = 10.
i = 1


def f(e):
    value = ((m.tan(a * (1 - e) ** (1 / 2))) ** (-1)) - ((1 / e) - 1) ** (1 / 2)
    return value


def df(e):
    value = a / (2 * (1 - e) ** (1 / 2) * (m.sin(a * (1 - e) ** (1 / 2))) ** 2) + 1 / (
            2 * e ** 2 * (1 / e - 1) ** (1 / 2))
    return value


def scan_n():
    p = 1
    while 1.0 != 1.0 + p:
        pp = p
        p /= 2
    N_max = a / (m.pi)
    print("N_max:")
    print(int(N_max) - 1)
    print("Enter the required energy level, less then N_max\n")
    global N
    N = int(input())
    if N > N_max:
        print("Enter N less then N_max\n")
        N = int(input())
        l = 1 - m.pi ** 2 * (N + 1) ** 2 / (a ** 2) + pp
        r = 1 - m.pi ** 2 * N ** 2 / (a ** 2) - pp
    else:
        l = 1 - m.pi ** 2 * (N + 1) ** 2 / (a ** 2) + pp
        r = 1 - m.pi ** 2 * N ** 2 / (a ** 2) - pp
    i = 0
    x = r
    while x > l:
        i += 1
        x1 = x
        x = x1 - f(x1) / (df(x1))
        print(x)
        if (abs(x - x1) < 10 ** (-10)) and abs(f(x)) < 10 ** (-5):
            break
    print(i)
    print(l, r)
    print(x1)
    print(f(x1))


scan_n()
