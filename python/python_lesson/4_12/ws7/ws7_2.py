# @d: positive integer value; @k: new base
# return a string representing d as a bas k number
def d2k(d, k):
    result = ""
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while d>0:
        digit = mapping[d%k]
        result = digit+ result
        d = d // k
    return result