# call function by the name
# everything is an object in python

def f1():
    print("1")
 
a = {"12": f1}

b=a["12"]
b
# <function f1 at 0x107a6d1e0>
b()
# 1