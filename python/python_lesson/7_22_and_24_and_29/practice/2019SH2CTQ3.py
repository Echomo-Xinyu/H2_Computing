class Node():
    def __init__(self, data):
        # link1: previous node; link2: next node
        self.data = data
        self.link1 = None
        self.link2 = None

    def print(self):
        # print(self.data)
        print("DATA: {0:5}; LINK1: {1:5}; LINK2: {2:5}".format(
            self.data, self.link1.data if self.link1 else "None",
            self.link2.data if self.link2 else "None"))


class DLNode(Node):
    def __init__(self, data):
        super.__init__(data)

    def print(self):
        print("\tDATA: {0:5}\n\tPREV: {1:5}\n\tNEXT: {2:5}".format(
            self.data, self.link1.data if self.link1 else "None",
            self.link2.data if self.link2 else "None"))


class BSTNode(Node):
    def __init__(self, data):
        # link1: left node; link2: right node
        super().__init__(data)

    def print(self):
        print("KEY: {0:5}\nBST.DATA:\n{1:5}\nLEFT: {2:5}\nRIGHT: {3:5}".format(
            self.data[0], self.data[1],
            self.link1.data[0] if self.link1 else "None",
            self.link2.data[0] if self.link2 else "None"))


class DLL():
    def __init__(self):
        self.first = None

    def insertFront(self, data):
        newNode = DLNode(data)
        if not self.first:
            self.first = newNode
            return
        newNode.link2, self.first.link1 = self.first, newNode
        self.first = newNode
        return

    def contains(self, data):
        if not self.first:
            return False
        currentNode = self.first
        while currentNode and currentNode.data != data:
            currentNode = currentNode.link2
        if currentNode == None:
            return False
        return True

    def print(self):
        if not self.first:
            print("Empty DLL")
            return
        currentNode = self.first
        while currentNode:
            currentNode.print()
            print(" -> ", end="")
            currentNode = currentNode.link2


class HT():
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]

    def _hash(self, data):
        return hash(data) % self.size

    def insert(self, data):
        location = hash(data)
        if not self.array[location]:
            self.array[location] = DLL()
        self.array[location].insertFront(data)
        return True

    def contains(self, data):
        location = hash(data)
        if not self.array[location]:
            return False
        return self.array[location].contains(data)

    def print(self):
        for i in range(self.size):
            if self.array[i] and self.array[i]._root == None:
                print("Index: "+str(i))
                self.array[i].print()
        
class Word(str):
    def __init__(self, string):
        self = string
    def __hash__(self):
        hashvalue = 0
        for i in range(len(self)):
            hashvalue += ord(self[i]) * (i+1)
        return hashvalue
    def print(self):
        print(self.upper())


def BST():
    def __init__(self):
        self._root = None

    def _insertNew(self, String):
        newHT = HT(1000)
        self.insert(String, newHT)
    
    def insert(self, data):
        pass
