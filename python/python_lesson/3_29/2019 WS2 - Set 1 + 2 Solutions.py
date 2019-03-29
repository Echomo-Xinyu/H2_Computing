#1
def prtItr(n):
    for i in range(len(n + 1)):
        print(i)

def prtRecMain(i, n):
    if i == n:
        print(i)
    else:
        print(i)
        prtRecMain(i + 1, n)

def prtRec(n):
    prtRecMain(0, n)



#2
def multiplyItr(a, b):
    # accounting for negative integer values
    sign = 1
    if a < 0:
        sign = -sign
        a = -a
    if b < 0:
        sign = -sign
        b = -b

    # calculate absolute product
    res = 0
    for i in range(a):
        res += b
    if sign < 0:
        return -res
    else:
        return res

def multiplyAbsRec(a, b):
    if a == 0:
        return 0
    elif a == 1:
        return b
    else:
        return b + multiplyAbsRec(a - 1, b)

def multiplyRec(a, b):
    # accounting for negative integer values
    sign = 1
    if a < 0:
        sign = -sign
        a = -a
    if b < 0:
        sign = -sign
        b = -b

    return sign * multiplyAbsRec(a, b)



#3
def sumItr(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

def sumRec(n):
    if n == 1:
        return 1
    else:
        return n + sumRec(n - 1)



#4
words = ["zero", "one", "two", "three", "four", "five", \
         "six", "seven", "eight", "nine", "ten"]
    
def digitWordsItr(n):
    global words
    n = str(n)
    for i in range(len(n)):
        if i == len(n) - 1:
            print(words[int(n[i])])
        else:
            print(words[int(n[i])], end = " ")

def digitWordsRecMain(n):
    global words
    if len(n) == 0:
        return ""
    elif len(n) == 1:
        return words[int(n)]
    else:
        return words[int(n[0])] + " " + digitWordsRecMain(n[1:])
    
def digitWordsRec(n):
    n = str(n)
    print(digitWordsRecMain(n))



#5
def prtRevItr(n):
    for i in range(n, -1, -1):
        print(i)

def prtRevRec(n):
    if n == 0:
        print(n)
    else:
        print(n)
        prtRevRec(n - 1) 



#6
def facItr(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def facRec(n):
    if n == 1:
        return 1
    else:
        return n * facRec(n - 1)



#7
def expItr(x, n):
    if n == 0:
        return 1
    else:
        res = 1
        neg = False
        if n < 0:
            n = -n
            neg = True
        for i in range(n):
            res *= x
        return 1/res if neg else res

def expRecMain(x, n):
    if n == 1:
        return x
    else:
        return x * expRecMain(x, n - 1)

def expRec(x, n):
    if n == 0:
        return 1
    else:
        neg = False
        if n < 0:
            n = -n
            neg = True
        return 1/expRecMain(x, n) if neg else expRecMain(x, n)



#8
def countDigitsItr(n):
    digits = 0
    while n > 0:
        digits = digits + 1
        n = n // 10
    return digits

def countDigitsRec(n):
    if n == 0:
        return 0
    else:
        return 1 + countDigitsRec(n // 10)



#9
def revStrItr(s):
    if len(s) < 2:
        return s
    else:
        res = ""
        for i in range(len(s)):
            res = s[i] + res
        return res

def revStrRec(s):
    if len(s) < 2:
        return s
    else:
        return revStrRec(s[1:]) + s[0]



#10
def sumListItr(L):
    sum = None # empty list is defined as having no sum
    for i in range(len(L)):
        if sum != None:
            sum += L[i]
        else:
            sum = L[i]
    return sum

def sumListRec(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    else:
        return L[0] + sumListRec(L[1:])



#11
def avgItr(L):
    avg = None # empty list is defined as having no average
    total = len(L)
    for i in range(len(L)):
        if avg != None:
            avg += L[i] / total
        else:
            avg = L[i] / total
    return avg

def avgRec(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    else:
        return sumListRec(L) / len(L)



#12
def minItr(L):
    if len(L) == 0:
        return None # empty list is defined as having no min
    elif len(L) == 1:
        return L[0]
    else:
        minVal = L[0]
        for i in range(1, len(L)):
            if L[i] < minVal:
                minVal = L[i]
        return minVal

def minRecMain(L, minVal):
    if len(L) == 1:
        return L[0] if L[0] < minVal else minVal
    else:
        return minRecMain(L[1:], L[0] if L[0] < minVal else minVal)

def minRec(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    else:
        return minRecMain(L[1:], L[0])



#13
def fibItr(n):
    F = [0, 1]
    while len(F) <= n:
        F.append(F[-1] + F[-2])
    return F[n]

def fibRec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRec(n - 2) + fibRec(n - 1)



#14
def isPrimeItr(n):
    if n < 2:
        return False
    isFactor = False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            isFactor = True
            break
    return not isFactor

def isPrimeRecMain(n, factor):
    if factor < 2:
        return True
    else:
        return False if n % factor == 0 else isPrimeRecMain(n, factor - 1)

def isPrimeRec(n):
    if n < 2:
        return False
    else:
        return isPrimeRecMain(n, int(n ** 0.5))
    
        

#15
def HCFItr(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    else:
        minVal = min(L)
        for i in range(minVal, 0, -1):
            isFacAll = True
            for j in range(len(L)):
                if L[j] % i != 0:
                    isFacAll = False
                    break
            if isFacAll:
                return i
            
def HCFRecMain(L, fac):
    isFacAll = True
    for i in range(len(L)):
        if L[i] % fac != 0:
            isFacAll = False
            break
    if isFacAll:
        return fac
    else:
        return HCFRecMain(L, fac - 1)

def HCFRec(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]
    else:
        return HCFRecMain(L, min(L))
