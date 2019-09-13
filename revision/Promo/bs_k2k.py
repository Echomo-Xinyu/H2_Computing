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

def bsI(L, target):
    length = len(L)
    l, r = 0, length-1
    # note the equal sign here
    while l <= r:
        # update mid value accordingly
        mid = (l + r) // 2
        if L[mid] == target:
            return True
        elif L[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return False

A = [1, 2, 3, 4, 5, 6, 8, 9, 10]
counter = 0
for i in range(len(A)):
    if bs(A, A[i]):
        counter += 1
if counter == len(A):
    print("nice")
    
counter = 0
for i in range(len(A)):
    if bsI(A, A[i]):
        counter += 1
if counter == len(A):
    print("nice")

# take capital letter
def d2k(num, k):
    result = ""
    mapping ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while num > 0:
        digit = num % k
        result = mapping[digit] + result
        num = num // k
    return result
print(d2k(10, 2))

def k2d(string, k):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for i in range(len(string)):
        result += mapping.index(string[i]) * k ** (len(string) - i - 1)
    return result

print(k2d("1010", 2))
