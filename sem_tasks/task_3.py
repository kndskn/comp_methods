from math import *

# Define functions


def f1(x): return 1. / (1 + x ** 2)


def f2(x): return x ** (1 / 3) * exp(sin(x))


# Define constants

a1 = -1.
b1 = 1.
a2 = 0.
b2 = 1.
n1 = 4
n2 = 8
n3 = 1024


def integrate_trapeze_method(f, a, b, n):
    result = 0
    h = (b - a) / n
    for i in range(1, n):
        result += f((b - a) / n * i + a) * h
    result += 0.5 * h * (f(a) + f(b))
    return result


def integrate_simpson_method(f, a, b, n):
    result = 0
    h = (b - a) / n
    for i in range(1, n, 2):
        result += 4 * f((b - a) / n * i + a) * h / 3
    for i in range(2, n, 2):
        result += 2 * f((b - a) / n * i + a) * h / 3
    result += h * (f(a) + f(b)) / 3
    return result


def print_results():
    print('Trapeze method:\n')
    print('I1 = ', integrate_trapeze_method(f1, a1, b1, n1), f'with {n1} steps')
    print('Accuracy = ', pi / 2 - integrate_trapeze_method(f1, a1, b1, n1), f'with {n1} steps')
    print('I1 = ', integrate_trapeze_method(f1, a1, b1, n2), f'with {n2} steps')
    print('Accuracy = ', pi / 2 - integrate_trapeze_method(f1, a1, b1, n2), f'with {n2} steps')
    print('I1 = ', integrate_trapeze_method(f1, a1, b1, n3), f'with {n3} steps')
    print('Accuracy = ', pi / 2 - integrate_trapeze_method(f1, a1, b1, n3), f'with {n3} steps\n')
    print('I2 = ', integrate_trapeze_method(f2, a2, b2, n1), f'with {n1} steps')
    print('I2 = ', integrate_trapeze_method(f2, a2, b2, n2), f'with {n2} steps')
    print('I2 = ', integrate_trapeze_method(f2, a2, b2, n3), f'with {n3} steps')
    print('\n\nSimpson method:\n')
    print('I1 = ', integrate_simpson_method(f1, a1, b1, n1), f'with {n1} steps')
    print('Accuracy = ', pi / 2 - integrate_simpson_method(f1, a1, b1, n1), f'with {n1} steps')
    print('I1 = ', integrate_simpson_method(f1, a1, b1, n2), f'with {n2} steps')
    print('Accuracy = ', pi / 2 - integrate_simpson_method(f1, a1, b1, n2), f'with {n2} steps')
    print('I1 = ', integrate_simpson_method(f1, a1, b1, n3), f'with {n3} steps')
    print('Accuracy = ', pi / 2 - integrate_simpson_method(f1, a1, b1, n3), f'with {n3} steps\n')
    print('I2 = ', integrate_simpson_method(f2, a2, b2, n1), f'with {n1} steps')
    print('I2 = ', integrate_simpson_method(f2, a2, b2, n2), f'with {n2} steps')
    print('I2 = ', integrate_simpson_method(f2, a2, b2, n3), f'with {n3} steps')


def main():
    print_results()


if __name__ == '__main__':
    main()
