# power function, x**n

def exponentiate1(n, m):
    if n==1:
        return m
    return m * exponentiate1(n-1, m)

print(exponentiate1(9, 10))

def exponentiate2(n, m):
    result = 1
    for i in range(n):
        result *= m
    return result

print(exponentiate2(9, 10))