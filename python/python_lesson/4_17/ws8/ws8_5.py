# @L: a list of floats
# quick sort in asscending order
def qs(L):
    n = len(L)
    if n < 2:
        return L
    pivot = L[0]
    more, less = [], []
    for i in range(1, n):
        if L[i] >= pivot:
            more.append(L[i])
        else:
            less.append(L[i])
    return qs(less) + [pivot] + qs(more)

def processL(L):
    sortedL = qs(L)
    n = len(sortedL)
    print("Minimum: " + str(sortedL[0]))

    if n % 2 == 0:
        median = (sortedL[n//2-1] + sortedL[n//2])/2
        if n % 4 == 0:
            first_quartile = (sortedL[n//4-1] + sortedL[n//4])/2
            third_quartile = (sortedL[n-1-n//4] + sortedL[n-n//4])/2
        else: # n % 4 == 2
            first_quartile = sortedL[n//4]
            third_quartile = sortedL[n-1-n//4]
    else:
        median = sortedL[(n-1)//2]
        # seperate then get two even length array
        if n % 4 == 1:
            first_quartile = sortedL[n//4]
            third_quartile = sortedL[n-n//4-1]
        else: # n % 4 == 3
            first_quartile = (sortedL[n//4-1] + sortedL[n//4])/2
            third_quartile = (sortedL[n-1-n//4] + sortedL[n-n//4])/2
    print("First Quartile: " + str(first_quartile))
    print("Median: " + str(median))
    print("Third Quartile: " + str(third_quartile))
    
    print("Maximum: " + str(sortedL[n-1]))