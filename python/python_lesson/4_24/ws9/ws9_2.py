# this file is to implement a node-based doubly-linked list (DLLL)
class DListNode:
    def __init__(self, data=None, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next
    
    def getPrevNode(self):
        return self._prev
    
    def setPrevNode(self, Node):
        self._prev = Node
    
    def getData(self):
        return self._data
    
    def setData(self, data):
        self._data = data
    
    def getNextNode(self):
        return self._next
    
    def setNextNode(self, Node):
        self._next = Node

    def __repr__(self):
        return repr(self.getData())


class DoublyLinkedList:
    def __init__(self):
        self._first = None
    
    def getRoot(self):
        return self._first
    
    def setRoot(self, data):
        newNode = DListNode(data)
        self._first = newNode
    
    def isEmpty(self):
        return self.getRoot() == None
    
    def insertFront(self, data):
        newNode = DListNode(data=data, next=self.getRoot())
        if self.getRoot():
            current = self.getRoot()
            current.setPrevNode(newNode)
        self.setRoot(newNode)

    def insertBack(self, data):
        newNode = DListNode(data=data)
        if not self.getRoot():
            self.setRoot(newNode)
        else:
            current = self.getRoot()
            while current.getNextNode():
                current = current.getNextNode()
            current.setNextNode(newNode)
            newNode.setPrevNode(current)
    
    def exists(self, data):
        if not self.getRoot():
            return False
        current = self.getRoot()
        while current and current.getData() != data:
            current = current.getNextNode()
        if current:
            return False
        else:
            return True
    
    def getNode(self, data):
        if not self.getRoot():
            return None
        current = self.getRoot()
        while current and current.getData() != data:
            current = current.getNextNode()
        return current # will be none if not found
    
    def delete(self, data):
        # if the DLLL is empty
        if not self.getRoot():
            return False
        current = self.getRoot()
        # if first element is to be deleted
        if current.getData() == data:
            self.setRoot(current.getNextNode())
            current.setPrevNode = None
            return True
        while current and current.getData() != data:
            current = current.getNextNode()
        if not current:
            return False
        else:
            current.getPrevNode().setNextNode(current.getNextNode)
            current.getNextNode().setPrevNode(current.getPrevNode)
            current.setPrevNode(None)
            current.setNextNode(None)
    
    def reverse(self):
        current = self.getRoot()
        prev_node = None
        while current:
            # prev_node means the nextx node in the unchanged DLLL
            prev_node = current.getPrevNode()
            current.setPrevNode(current.getNextNode())
            current.setNextNode(prev_node)
            current = current.getPrevNode()
        # check the condition if DLLL is empty 
        if prev_node is not None:
            self.setRoot(prev_node.getPrevNode())
    
    def __repr__(self):
        if not self.getRoot():
            return "Empty"
        else:
            result = ""
            current = self.getRoot()
            while current:
                result += str(current) + "\n"
                current = current.getNextNode()
            return result