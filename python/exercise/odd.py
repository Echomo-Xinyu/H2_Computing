n = int(input("Enter n: "))
lis = []
for i in range(1, n+1, 2):
    # print(str(i))
    lis.append(i)
print(lis[2:10:3])