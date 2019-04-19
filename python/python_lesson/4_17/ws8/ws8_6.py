# the menu
print("1. Read file data")
print("2. Bubble sort")
print("3. Quick sort / Insertion sort")
print("4. End")

# read the file data (Option 1)
handle = open("ADMISSIONS-DATA.TXT", "r")
data = []
for line in handle:
    if line != None:
        num = line.strip().split(",")
        data.append(num)

# bubble sort (Option 2)
def bubbleSort(L):
    counter_comparison = 0
    n = len(L)
    for i in range(n-1):
        for j in range(n-i-1):
            counter_comparison += 1
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L, counter_comparison

# quick sort (Option 3)
counter_comparison = 0
def quickSort(L):
    n = len(L)
    if n < 2:
        return L
    pivot = L[0]
    more, less = [], []
    for i in range(1, n):
        counter_comparison += 1
        if L[i] >= pivot:
            more.append(L[i])
        else:
            less.append(L[i])
    return quickSort(less) + [pivot] + quickSort(more)

print(counter_comparison)