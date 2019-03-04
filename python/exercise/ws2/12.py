# return minimum of list

def mini1(mylist):
    minim = 10*10
    for i in range(len(mylist)):
        if minim > mylist[i]:
            minim = mylist[i]
    return minim

def mini2(mylist, n=0, min=10000000000):
    if mylist[n]<min:
        min = mylist[n]
    if n+1==len(mylist):
        return min
    return mini2(mylist, n+1, min)

print(mini2([1, 2, 0.1, 3, 4]))
    
