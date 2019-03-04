# number of digits in n

def length1(n):
    count = 0
    while (n!=0):
        n = n // 10
        count += 1
    return count

print(length1(10000))

def length2(n):
    if n==0:
        return 0
    return length2(n//10)+1
print(length2(100000))