# return factorial

def fac1(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def fac2(n):
    if (n==1):
        return 1
    return n * fac2(n-1)

print(fac1(10))
print(fac2(10))
# 3628800