# @L: a list of integers
# insertion sort in asscending order
def insertionSort(L):
    n = len(L)-1
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
    return L

L = [1, 9, 2, 6, 3, 2, 4, 5, 1]
print(insertionSort(L))