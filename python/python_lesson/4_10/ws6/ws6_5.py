# @L: list of integer; @t: the target integer
# the function is to return the index of the element just smaller than t
def linearSearch3(L, t):
    s_min_t, index = t, -1
    n = len(L)
    for i in range(n):
        if L[i]<t and s_min_t<L[i]:
            s_min_t, index = L[i], i
    return index