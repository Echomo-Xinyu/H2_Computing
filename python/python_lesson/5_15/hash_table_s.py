# this file is to implement a simple version of hash table
class HashTable():
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]
    
    def insert(self, data):
        target = hash(data) % self.size
        end = target
        while True:
            if self.array[target] == None:
                self.array[target] = data
                return
            else:
                target = (target + 1) % self.size
                if target == end:
                    # print error message
                    return
    
    # to make the code modular
    def getIndex(self, data):
        target = hash(data) % self.size
        end = target
        while self.array[target] != data:
            target = (target + 1) % self.size
            if target == end:
                return -1
        return target

    def exists(self, data):
        return self.getIndex(data)!=-1
    
    def delete(self, data):
        target = self.getIndex(data)
        if target==-1:
            return False
        else:
            self.array[target] = None
            return True
    
    def print(self):
        for i in range(self.size):
            print(str(i) + ": " + str(self.array[i]))
