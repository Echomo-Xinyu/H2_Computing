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

    def insertFront(self, data):
        newNode = Node(data)
        newNode.setNext(self._root)
        self.setRoot(newNode)

    def insertBack(self, data):
        newNode = Node(data)
        if not self._root:
            self.setRoot(newNode)
        else:
            current = self._root
            # line below is equivalent to while current.next != None:
            while current.getNext():
                current = current.getNext()
            current.setNext(newNode)

    def exists(self, data):
        if not self._root:
            return False
        current = self._root
        while current and current.getData() != data:
            current = current.getNext()
        # if check the data here, it may throw a exception as it may be a None, and None.data gives a exception 
        # equivalent to current == None
        if not current:
            return False
        else:
            return True

    def getNode(self, data):
        if not self._root:
            return None
        current = self._root
        while current and current.getData() != data:
            current = current.getNext()
        return current


    def delete(self, data):
        if not self._root:
            return False
        current = self._root
        if current.getData() == data:
            self.setRoot(current.getNext())
            return True
        else:
            while current.getNext() and current.getNext().getData() != data:
                current = current.getNext()
            if current.getNext():
                return False
            else:
                current.setNext(current.getNext().getNext())
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
