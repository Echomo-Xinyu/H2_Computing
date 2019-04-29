# this file is to store a modular version of SLLL, DLLL and CDLLL
class node():
    def __init__(self, data=None, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data

    def getNextNode(self):
        return self._next

    def setNextNode(self, node):
        self._next = node

    def getPrevNode(self):
        return self._prev

    def setPrevNode(self, node):
        self._prev = node

    def __str__(self):
        return str(self._data)


class SLLL():
    def __init__(self):
        self._root = None

    def getRoot(self):
        return self._root

    def setRoot(self, node):
        self._root = node

    def isEmpty(self):
        return self._root == None

    def insertFront(self, data):
        newNode = node(data=data, next=self.getRoot())
        self.setRoot(newNode)

    def insertBack(self, data):
        newNode = node(data=data)
        if not self.getRoot():
            self.setRoot(newNode)
        else:
            current = self.getRoot()
            while current.getNextNode():
                current = current.getNextNode()
            current.setRoot(newNode)

    def exists(self, data):
        if not self.getRoot():
            return False
        current = self.getRoot()
        while current and current.getData() != data:
            current = current.getNextNode()
        if not current:
            return False
        else:
            return True

    def getNode(self, data):
        if not self.getRoot():
            return None
        current = self.getRoot()
        while current and current.getData != data:
            current = current.getNextNode()
        return current

    def delete(self, data):
        if not self.getRoot():
            return False
        current = self.getRoot()
        # first node is to be deleted
        if current.getData() == data:
            self.setRoot(current.getNextNode())
            return True
        while current.getNextNode() and current.getNextNode().getData() != data:
            current = current.getNextNode()
        if not current.getNextNode():
            return False
        else:
            current.setNextNode(current.getNextNode().getNextNode())
            return True

    def __str__(self):
        if not self.getRoot():
            return "Empty"
        result = ""
        current = self.getRoot()
        while current:
            result += str(current) + " "
            current = current.getNextNode()
        return result


class DLLL(SLLL):
    def insertFront(self, data):
        newNode = node(data=data, next=self.getRoot())
        if self.getRoot():
            self.getRoot().setPrevNode(newNode)
        self.setRoot(newNode)
    # after implementing the .insertFront() function
    # i feel its pretty close to what it is like to write a whole new thing? 


class CDLLL(DLLL):
    pass
