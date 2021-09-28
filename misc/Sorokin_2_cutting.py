import math as m

i = 1
j = 1
global pp
p = 1

while 1.0 != 1.0 + p:
    pp = p
    j += 1
    p /= 2


def f(e):
    value = ((m.tan(a * (1 - e) ** (1 / 2))) ** (-1)) - ((1 / e) - 1) ** (1 / 2)
    return value


def scan_n():
    global l, r, a
    print("Enter const a\n")
    a = float(input())
    N_max = a / (m.pi)
    print("N_max:")
    print(int(N_max) - 1)
    print("Enter the required energy level, less then N_max\n")
    N = int(input())
    if (N > N_max):
        print("Enter N less then N_max\n")
        N = int(input())
        l = 1 - m.pi ** 2 * (N + 1) ** 2 / (a ** 2) + pp
        r = 1 - m.pi ** 2 * N ** 2 / (a ** 2) - pp
    else:
        l = 1 - m.pi ** 2 * (N + 1) ** 2 / (a ** 2) + pp
        r = 1 - m.pi ** 2 * N ** 2 / (a ** 2) - pp
    print(l, r)


def diff():
    i = 0
    dx = (r - l) / 100
    x = r
    while True:
        i += 1
        x1 = x
        if (x1 + dx) > r:
            x = x1 - f(x1) * dx / (f(x1) - f(x1 - dx))  # пытался реальзовать метод Секущих, то есть подсчет
            # геометрической производной на каждом шаге
        else:
            x = x1 - f(x1) * 2 * dx / (f(x1 + dx) - f(x1 - dx))
        if (abs(x - x1) < 10 ** (-10)) and abs(f(x1)) < 10 ** (-5):
            break

    print(i)
    print(x1)
    print(f(x1))


scan_n()
diff()
