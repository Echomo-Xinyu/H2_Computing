# return sum of input list element

def sum1(mylist):
    sum = 0
    for i in range(len(mylist)):
        sum += mylist[i]
    return sum


def sum2(mylist, n):
    if n==-1:
        return 0
    return mylist[n]+sum2(mylist, n-1)

n = 5
lis = [1, 2, 3, 4, 5, 6]

print(sum1(lis))
print(sum2(lis, n))
