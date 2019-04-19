# @L: a list of integers; @t: a target integer
# the function is to find the index of element in L just greater than t
def linearSearch2(L, t):
    s_max_t, index = t, -1
    n = len(L)
    for i in range(n):
        if L[i]>t and s_max_t>L[i]:
            s_max_t, index = L[i], i
    return index