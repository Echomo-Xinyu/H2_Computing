# greatest common divisor of a set of positive integers

def gcd_1(my_list):
    minimum = 10000000000
    # whether_gcd = True
    for i in my_list:
        if i<minimum:
            minimum = i
            # print("minimum: " + str(minimum))
    for i in range(minimum+1, 0, -1):
        whether_gcd = True
        for j in my_list:
            if j%i!=0:
                whether_gcd = False
                break
        if whether_gcd:
            return i


# m: the divisor to check; n: index
def is_divisor(mylist, m, n=0):
    if n+1==len(mylist):
        return True
    if mylist[n]%m != 0:
        return False
    else:
        return is_divisor(mylist, m, n+1)

def mini2(mylist, n=0, min=10000000000):
    if mylist[n]<min:
        min = mylist[n]
    if n+1==len(mylist):
        return min
    return mini2(mylist, n+1, min)

def gcd_2(my_list, a=0):
    if a==0:
        a = mini2(my_list)
    if is_divisor(my_list, a, 0):
        return a
    else:
        return gcd_2(my_list, a-1)

print(gcd_2([3, 4, 5, 6]))
    