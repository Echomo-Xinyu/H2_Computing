# the file is to write two ways to compute all the subset of a given list
class Stack():
    def __init__(self):
        pass
    def size(self):
        return 0
    def push(self, data1, data2):
        return
    def pop(self):
        return (0, 1)

def permute(s):
    temp = Stack()
    result = []
    temp.push("", s)
    while True:
        if temp.size() <= 0:
            return result
        current = temp.pop()
        if len(current[2]) == 0:
            result.append(current[0])
        else:
            i = 1
            while i <= len(current[2]):
                length = len(current[2])
                a = current[0] + current[2][i]
                b = current[:i-1] + current[i:length]
                temp.push(a, b)
                i = i + 1

