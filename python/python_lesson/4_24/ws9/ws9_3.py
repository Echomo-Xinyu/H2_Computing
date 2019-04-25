# This file is to implement a node-based circular doubly-linked linked list
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

class DList():
    def __init__(self):
        self._root = None