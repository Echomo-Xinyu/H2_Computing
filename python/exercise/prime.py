import math

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, math.sqrt(n)):
        if n%i==0:
            return False
    return True

count=0
input_n = int(input("Please input the nth prime you want to know: \n"))

# some random huge number
for i in range(2, 1000000):
    if is_prime(i):
        count+=1
    if count==input_n:
        break

print(str(i))

# sieve method
def sieve(n: int) -> list:
    """
    Sieve away and only primes are left.
    """
    primes = 2*[False] + (n-1)*[True]
    for i in range(2, int(n**0.5+1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]