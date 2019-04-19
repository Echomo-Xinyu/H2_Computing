# @s: a positive integer in the base @k
# return integer corresponding s value in base 10
def k2d(s, k):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for i in range(len(s)):
        result = mapping.index(s[i]) * k ** (len(s)-1-i)
    return result