# @L: ascending sorted list of integerd; @t: target integer
# the function will return the index of any instance 
# in L that is just greater than t, else return -1
def binarySearch3(L, t):
    l, r = 0, len(L)-1
    while (l<=r):
        mid = (l+r) // 2
        if L[mid] == t:
            if mid+1 <= len(L)-1:
                return mid+1
            else:
                return -1
        elif L[mid] > t:
            r = mid - 1
        else:
            l = mid + 1
    if l > len(L) - 1:
        return -1
    else:
        return l


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch3(L, 10.7))