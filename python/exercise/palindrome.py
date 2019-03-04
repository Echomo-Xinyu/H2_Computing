def reverse(s):
    str = ""
    for i in s:
        str = i+str
    return str

def palindrome(s):
    x = len(s)//2+1
    y = len(s)//2
    print(s[0:x]==reverse(s[y:]))

palindrome("HEH")
