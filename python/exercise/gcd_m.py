# to compute the gcd of a list of integers

# iterative version
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

# not quite sure how to write recursive version
def gcd_c(my_list):
    return 1

print(gcd_1([1, 100, 50, 30, 26]))
