# merge sort
def mergeSort(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        left = arr[:mid].copy()
        right = arr[:mid].copy()
        left = mergeSort(left)
        right = mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j+= 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[j] = right[j]
            k += 1
            j += 1
    return arr

# quick sort
def quickSort(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    less, more = [], []
    for i in range(1, len(L)):
        if L[i] < pivot:
            less.append(L[i])
        else:
            more.append(L[i])
    return quickSort(less) + [pivot] + quickSort(more)