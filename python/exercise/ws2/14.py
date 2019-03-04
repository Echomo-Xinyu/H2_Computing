# whether prime
import math

def is_prime1(n):
    if n<=1:
        return False
    for i in range(2, math.sqrt(n)):
        if n%i==0:
            return False
    return True

def is_prime2(n, m):
    if m==2:
        return True
    if n%m==0:
        print(m)
        return False
    return is_prime2(n, m-1)

a = int(math.sqrt(1037))
print(is_prime2(1037, a))


