# print number from 0 to the input

a = int(input("Give me a posituve integer: \n"))

def output1(m):
    if (m==0):
        print(0)
        return
    output1(m-1)
    print(m)

def output2(m):
    for i in range(0, m+1):
        print(i)

output1(a)

output2(a)