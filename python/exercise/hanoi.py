# The file is for a question about hanoi tower
# The goal is to list down the process to move all the rings from a to c

a, b, c = "a", "b", "c"
def hanoi(n, a, b, c):
    if n == 1:
        print(a, n, c)
    else:
        # print("a", n-1, "b")
        hanoi(n-1, a, c, b)
        print(a, n, c)
        hanoi(n-1, b, a, c)

hanoi(3, a, b, c)