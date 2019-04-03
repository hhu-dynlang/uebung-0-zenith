

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
        print("iteration {:d}, crud={:s}".format(i, str(crud)))
    return crud


def flatten(list):
    flatlist = []
    for i in list:
        if not hasattr(i, '__iter__'):
            flatlist += [i]
        else:
            flatlist += flatten(i)
    return flatlist
