# return mean of number in list

def mean1(mylist):
    count = len(mylist)
    sum = 0.0
    for i in range(len(mylist)):
        sum += mylist[i]
    return sum / count

print(mean1([1, 2, 3.0, 6]))

# # i only know to implement count and sum recursively and then divide
# # mean2() function and don't know how to implement mean2()
def mean2(mylist, n=0, sum=0.0):
    sum += mylist[n]
    if n+1==len(mylist):
        return sum / len(mylist)
    return mean2(mylist, n+1, sum)

print(mean2([1, 2, 3.0, 6]))
    