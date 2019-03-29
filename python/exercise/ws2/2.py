# a multiply calculator, n * m, m1=m2

# the answer is incorrect as it ignores the negative
# integer input

def multiply1(n, m):
    if n==1:
        return m
    return m + multiply1(n-1, m) 

print(multiply1(6, 9))

def multiply2(n, m):
    sum = 0
    for i in range(1, n+1):
        sum += m
    return sum

print(multiply2(9, 6))