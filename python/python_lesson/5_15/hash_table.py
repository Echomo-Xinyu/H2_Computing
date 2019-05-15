# this is to implememnt an array-based hash table
# the data stored includes `key: value`, inspired by dictionary in python
class HashTable():
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]

    # could be implement in a more elegant manner
    def hash(self, key):
        return hash(key) % self.size

    # hash the key, loop through to find an empty spot, insert the value
    def insert(self, key, value):
        target = self.hash(key)
        end = target
        while self.array[target] != None:
            target = (target + 1) % self.size
            if target == end:
                # print error message
                print("Hash Table full. Fail to insert")
                return
        self.array[target] = (key, value)

    def delete(self, key):
        target = self.hash(key)
        end = target
        while self.array[target] != None and self.array[target][0] != key:
            target = (target + 1) % self.size
            if target == end:
                print("Not exists")
                return False
        if not self.array[target]:
            return False
        else:
            self.array[target] = None
            return True

    # linear search
    def exists(self, key):
        target = self.hash(key)
        end = target
        while True:
            if self.array[target] != None and self.array[target][0] == key:
                return True
            target = (target + 1) % self.size
            if target == end:
                # print("Not exists")
                return False

    # three locations, 1st location insert a, b and 2nd location insert c,
    # offset to 3rd location
    # delete the b at the 2nd location and then search the c, case
    # do a linear search to address the limitation of imperfect hash function
    def search(self, key):
        target = self.hash(key)
        end = target
        while True:
            if self.array[target] != None and self.array[target][0] == key:
                return self.array[target]
            target = (target + 1) % self.size
            if target == end:
                print("Not exists")
                return

    def print(self):
        for i in range(self.size):
            print(i, self.array[i])
