# @L: list of integer, @t: target integer
def linearSearch1(L, t):
    n = len(L)
    for i in range(n):
        if L[i] == t:
            return i
    return -1