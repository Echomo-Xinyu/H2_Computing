'''
https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/
an article that clarifies the problem
'''


# EXAMPLE 1: immutable object, call by object, primitive data type: string, int, boolean
def f1(my_number):
    my_number+=1
    print("my_number is: " + str(my_number))

my_number = 10
f1(my_number)
print("my_number is: " + str(my_number))
# output:
# ... 11
# ... 10

# EXAMPLE 2: mutable object, call by object reference, such as list, dictionary, non-primitive object
def f2(my_list):
    my_list.append(10000)
    print("my_list is: " + str(my_list))

my_list = [1, 2, 3]
f2(my_list)
print("my_list is: " + str(my_list))
# output:
# ... [1,2,3,10000]
# ... [1,2,3,10000]

# similar case for EXAMPLE 2:
L1 = [1, 2, 3]
L2 = L1 # pass by object reference
L2[1] = 100
print(L1[1])
# output: 100

# to copy the value of the L1
L1 = [1, 2, 3]
L2 = L1[:] # L2 = L1[0:len(L1)]
# also L2 = L1.copy()
L2[1] = 100
print(L1[1])
# output: 2

print(L1==L2)
# True
print(L1 is L2)
# False
# for creating a copy and not referring to the same 