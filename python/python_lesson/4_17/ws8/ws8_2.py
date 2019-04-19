# @L: a list of integers
# bubbleSort in ascending order
def bubbleSort(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L