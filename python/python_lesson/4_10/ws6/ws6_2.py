# @L: list of ascending sorted integer, @t: target integer
def binarySearch1(L, t):
    l, r = 0, len(L)-1
    while (l<=r):
        mid = (l + r) // 2
        if L[mid] == t:
            return mid
        elif L[mid] > t:
            r = mid - 1
        else: #L[mid] < t:
            l = mid + 1
    return -1
