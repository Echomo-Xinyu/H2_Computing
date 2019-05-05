# this file is to implement a node-based singly-linked linked list (SLLL)
class Node():
    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return str(self._data)

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data

    def getNext(self):
        return self._next

    def setNext(self, Node):
        self._next = Node

    def print(self):
        print(self._data)


class linkedList():
    def __init__(self):
        self._root = None

    def getRoot(self):
        return self._root

    def setRoot(self, Node):
        self._root = Node

    def isEmpty(self):
        return self._root == None
    
    def size(self):
        if not self._root:
            return 0
        current = self._root
        count = 1
        while current:
            current = current.getNext()
            count += 1
        return count

    def insertSorted(self, data):
        newNode = Node(data)
        if not self._root:
            self._root = newNode
            return True
        currentNode = self._root
        while currentNode.getNext() and (currentNode.getData() <= data and data <= currentNode.getNext().getData()):
            currentNode = currentNode.getNext()
        currentNode.setNext(newNode)
        return True
        

    def print(self):
        if not self._root:
            return "Empty"
        else:
            result = ""
            current = self._root
            while current:
                result += str(current) + "\n"
                current = current.getNext()
            return result
