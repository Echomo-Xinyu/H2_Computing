# return reversed copy of a string

def reverse1(str):
    str1 = ""
    for i in range(len(str)-1, -1, -1):
        str1 += str[i]
    return str1

print(reverse1("peo"))

def reverse2(str):
    a = len(str)
    if a==0:
        return ""
    return str[a-1]+reverse2(str[:a-1])

print(reverse2("hello"))