# @L: a list of integer
# quick sort in asscending order
def qs(L):
    n = len(L)
    if n < 2:
        return L
    pivot = L[0]
    more, less = [], []
    for i in range(1, n):
        if L[i] >= pivot:
            more.append(L[i])
        else:
            less.append(L[i])
    return qs(less) + [pivot] + qs(more)

L = [1, 9, 2, 6, 3, 2, 4, 5, 1]
print(qs(L))