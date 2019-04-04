from math import log


def is_palindrome(s):
    lens = len(s)
    split = lens//2
    return s[0:split:1] == s[-1:(split-1 if (lens % 2 == 0) else split):-1]


def pascal(n):
    if n < 0:
        return []
    crud = [[1]]
    for i in range(1, n+1):
        tmp = [1]
        for j in range(0, i-1):  # could be halved, but im lazy
            tmp += [crud[i-1][j] + crud[i-1][j+1]]
        tmp += [1]
        crud += [tmp]
        # print("iteration {:d}, crud={:s}".format(i, str(crud)))
    return crud


def flatten(list):
    flatlist = []
    for i in list:
        flatlist += [i] if not hasattr(i, '__iter__') else flatten(i)
    return flatlist


def solve_equation(a, b, c):
    if a == 0:
        return {-c/b}
    tmp = b**2 - 4*a*c
    if tmp < 0:
        return {}  # no imaginary numbers, since i'm lazy
    tmp = tmp**(1/2)
    return {(tmp-b)/(2*a), (-b-tmp)/(2*a)}


def fizz_buzz(n):
    ret = []
    for i in range(1, n+1, 1):
        tmp = 'fizz' if i % 3 == 0 else ''
        if i % 5 == 0:
            tmp += 'buzz'
        ret += [tmp] if tmp else [i]
    return ret


def mybin(n):
    if n == 0:
        return '0b0'
    maxp = int(log(n, 2))
    ret = '0b1'
    n -= 2**maxp
    maxp -= 1
    while maxp >= 0:
        cp = 2**maxp
        if n >= cp:
            n -= cp
            ret += '1'
        else:
            ret += '0'
        maxp -= 1
    return ret


def myint(n):
    n = n[2::]
    lenn = len(n)
    ret = 0
    for p in range(lenn-1, -1, -1):
        ret += 2**p if int(n[lenn-p-1]) == 1 else 0
        # print("p: {:d}, ret: {:d}".format(p, ret))
    return ret
