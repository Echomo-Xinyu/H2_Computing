# return 1 + 2 + ... + input n

def sum1(n):
    if n==1:
        return 1
    return n+sum1(n-1)

print(sum1(10))

def sum2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum2(10))
