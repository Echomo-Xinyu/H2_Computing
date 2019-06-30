def binarySearch(sortedL, t):
    # l, r marks the left and right end of 
    # interval searching for the element
    l, r = 0, len(sortedL) - 1
    # note the equation sign
    while (l <= r):
        mid = (l + r) // 2
        if sortedL[mid] == t:
            return mid
        elif sortedL[mid] > t:
            r = mid - 1
        else:  # sortedL[mid] < t:
            l = mid + 1
    return -1

# recursive version for binary search
def binarySearchR(sortedL, t, l=0, r=10000):
    # a lazy approach in order not to write a wrap-up function
    if r==10000:
        r = len(sortedL) - 1
    if l > r:
        return -1
    mid = (l + r) // 2
    if sortedL[mid] == t:
        return mid
    elif sortedL[mid] < t:
        return binarySearchR(sortedL, t, mid+1, r)
    else:
        return binarySearchR(sortedL, t, l, mid-1)


lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(binarySearch(lis, 5))
print(binarySearchR(lis, 5))
print(binarySearchR(lis, 14))
print(binarySearchR(lis, 0))
