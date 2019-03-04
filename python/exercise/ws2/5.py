# outpur from input n to 0

def output1(n):
    if n==0:
        print(0)
        return
    print(n)
    output1(n-1)

def output2(n):
    for i in range(n, -1, -1):
        print(i)

output1(10)

output2(10)
