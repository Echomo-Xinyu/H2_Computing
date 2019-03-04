# fibonacci sequence

def f1(n):
    if n==1 or n==2:
        return 1
    return f1(n-1)+f1(n-2)

def f2(n):
    lis = [1, 1]
    for i in range(2, n+1):
        lis.append(lis[i-1]+lis[i-2])
    return lis[n-1]

print(f1(10))
print(f2(10))