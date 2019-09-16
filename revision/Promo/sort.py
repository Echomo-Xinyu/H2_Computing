# sorting algorithms: bubble sort, insert sort, quick sort & merge sort
# assume L in all function calls is a list with comparable objects
def bubbleSort(L):
    length = len(L)
    for i in range(length):
        for j in range(length - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


def bubbleSortQ(L):
    length = len(L)
    for i in range(length):
        whether_exchanged = False
        for j in range(length - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                whether_exchanged = True
        if whether_exchanged == False:
            break
    return L


def insertionSort(L):
    length = len(L)
    for i in range(length):
        for j in range(i, 0, -1):
            # here seem to be able to improve by ending when encountering anomalous case
            if L[j] < L[j - 1]:
                L[j], L[j - 1] = L[j - 1], L[j]
    return L


def quickSort(L):
    length = len(L)
    if length <= 1:
        return L
    pivot = L[0]
    less, more = [], []
    for i in range(1, length):
        if L[i] < pivot:
            less.append(L[i])
        else:
            more.append(L[i])
    return quickSort(less) + [pivot] + quickSort(more)


def qs(L):
    return (
        qs([L[i] for i in range(1, len(L)) if L[i] < L[0]]) + [L[0]] +
        qs([L[j]
            for j in range(1, len(L)) if L[j] >= L[0]])) if len(L) >= 2 else L


def mergeSort(L):
    length = len(L)
    if length > 1:
        mid = length // 2
        left = L[:mid]
        right = L[mid:]
        # make sure both halves' element are sorted
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1
        # check elements left
        while i < len(left):
            L[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            L[k] = right[j]
            k += 1
            j += 1
    return L


A = [1, 3, 4, 2, 5]
# A = bubbleSort(A)
# A = bubbleSortQ(A)
# A = insertionSort(A)
# A = quickSort(A)
# A = qs(A)
A = mergeSort(A)
for i in range(len(A)):
    print(A[i])
