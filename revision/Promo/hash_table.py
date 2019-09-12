# the file is to write a typical hash table
# collision case with deletion is not considered
class HT():
    def __init__(self, size=10):
        self.size = size
        self.array = [None for i in range(size)]
    def _hash(self, data):
        return hash(data) % self.size
    # shift to next if place taken
    def insert(self, data):
        target = self._hash(data)
        end = target
        while True:
            if self.array[target] == None:
                self.array[target] = data
                return True
            else:
                target = (target + 1) % self.size
                if target == end:
                    return False
    def findIndex(self, data):
        target = self._hash(data)
        end = target
        while True:
            if self.array[target] == data:
                return target
            else:
                target = (target + 1) % self.size
                if target == end:
                    return -1
    def exists(self, data):
        return self.findIndex(data) != -1
    def delete(self, data):
        index = self.findIndex(data)
        if index == -1:
            return False
        self.array[index] = None
        return True
    def print(self):
        for i in range(self.size):
            print(str(i) + " : " + str(self.array[i]))

# too lazy to write out test cases
