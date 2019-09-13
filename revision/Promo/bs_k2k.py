# the file is to implement a binary search, k2d and d2k algorithm
# assume @L is sorted list containing comparbale objects against @target
def bs(L, target):
    length = len(L)
    if length <= 0:
        return False
    mid = length // 2
    if L[mid] == target:
        return True
    elif target < L[mid]:
        return bs(L[:mid], target)
    else: # L[mid] < target
        return bs(L[mid:], target)

A = [1, 2, 3, 4, 5, 6, 8, 9, 10]
if bs(A, 8):
    print("hey")
if bs(A, 10):
    print("hey")
