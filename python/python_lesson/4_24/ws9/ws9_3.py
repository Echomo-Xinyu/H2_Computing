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

    def __str__(self):
        return str(self.getData())

# 
class DList1():
    def __init__(self):
        self._root = None
    # write two variants of the DList
    def getRoot(self):
        return self._root
    
    def setRoot(self, Node):
        self._root = Node
        Node.setNextNode(Node)
        Node.setPrevNode(Node)
    
    def isEmpty(self):
        return self._root == None
    
    def insertionFront(self, data):
        newNode = DListNode(data=data)
        if not self._root:
            self.setRoot(newNode)
            return 
        else:
            old_root = self._root
            newNode.setPrevNode(old_root.getPrevNode())
            old_root.getPrevNode().setNextNode(newNode)
            newNode.setNextNode(old_root)
            old_root.setPrevNode(newNode)
            return
    
    def insertionBack(self, data):
        newNode = DListNode(data=data)
        if not self._root:
            self.setRoot(newNode)
        else:
            old_last_node = self._root.getPrevNode()
            newNode.setPrevNode(old_last_node)
            old_last_node.setNextNode(newNode)
            newNode.setNextNode(self._root)
            self._root.setPrevNode(newNode)
    
    def exists(self, data):
        if not self._root:
            return False
        root = self._root
        if root.getData() == data:
            return True
        current = root.getNextNode()
        while current is not root and current.getData() != data:
            current = current.getNextNode()
        return current is not root
    
    def getNode(self, data):
        if not self._root:
            return None
        root = self._root
        if root.getData() == data:
            return root
        current = root.getNextNode()
        while current is not root and current.getData() != data:
            current = current.getNextNode()
        if current is root:
            return None
        else:
            return current
    
    def delete(self, data):
        if self._root == None:
            return False
        root = self._root
        if root.getData() == data:
            # the CDLLL has more than one element
            if root.getNextNode() is not root:
                root.getPrevNode().setNextNode(root.getNextNode())
                root.getNextNode().setPrevNode(root.getPrevNode())
            else:
                self._root = None
            return True
        current = root.getNextNode()
        while current is not root and current.getData() != data:
            current = current.getNextNode()
        # the node with node.data == data never found
        if current is root:
            return False
        else:
            current.getPrevNode().setNextNode(current.getNextNode())
            current.getNextNode().setPrevNode(current.getPrevNode())
            return True
    
    def __str__(self):
        if not self._root:
            return "Empty"
        result = ""
        current = self.getRoot()
        while current is not self._root:
            result = result + str(current) + "\n"
            current = current.getNextNode()
        return result

DL1 = DList1()
DL1.setRoot(DListNode(1))

print(DL1.getRoot())
print(DL1.isEmpty())
DL1.insertionFront(3)
DL1.insertionBack(2)
print(DL1.exists(2))
print(DL1.getNode(2))
print(DL1)
print(DL1.delete(1))
print(DL1.delete(2))
print(DL1.getRoot())
print(DL1.delete(4))
print(DL1.delete(3))
# print(DL1.delete(4))
print(DL1.getRoot())
DL1.insertionFront(3)
# print(DL1)
# print(DL1.getRoot())
DL1.insertionBack(2)
# print(DL1)
print(DL1)