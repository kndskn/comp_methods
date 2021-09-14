import numpy as np

_ONE = [np.float32(1.0)]
__ONE = [1.]
_ONES = []
__ONES = []
_COMP = ['1', '1 + e', '1 + e / 2', '1 + e + e / 2']


def find_upl32(num):
    count = 0
    while num[count] != np.float32(0.0):
        num.append(np.float32(1 + 1 / 2 ** count) - np.float32(1.0))
        count += 1
    return [num[count - 1], count - 2]


def find_upl64(num):
    count = 0
    while num[count] != 0.:
        num.append(float(1 + 1 / 2 ** count) - float(1.0))
        count += 1
    return [num[count - 1], count - 2]


def find_max(num):
    reslt = 0
    cnt = 0
    while not np.isinf(num[0]):
        reslt = num[0]
        num[0] = num[0] * 2
        cnt += 1
    return [reslt, cnt]


def find_max32(num):
    reslt = 0
    cnt = 0
    while not np.isinf(num[0]):
        reslt = num[0]
        num[0] = np.float32(num[0] * 2)
        cnt += 1
    return [reslt, cnt]


def comparison(one, ones, e):
    ones.append(one)
    ones.append(one + e)
    ones.append(one + e / 2)
    ones.append(one + e + e / 2)
    comp = dict(zip(_COMP, ones))
    return comp


def main():
    res1 = find_upl32(_ONE)
    res2 = find_upl64(__ONE)
    res_max_1 = find_max32(_ONE)
    res_max_2 = find_max(__ONE)
    print('Result_32', res1)
    print('Result_64', res2)
    print('Compare_32', comparison(_ONE[0], _ONES, res1[0]))
    print('Compare_64', comparison(__ONE[0], __ONES, res2[0]))
    print('Result_max32', res_max_1[0])
    print('Result_max64', res_max_2[0])
    print('Power_max32', res_max_1[1])
    print('Power_max64', res_max_2[1])


if __name__ == '__main__':
    main()
