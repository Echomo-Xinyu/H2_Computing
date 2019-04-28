# this file is to implement a node-based doubly-linked list (DLLL)
# as self._root is firstly initialized to be None, it may suggest errors in your IDE
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
        self._root = None

    def getRoot(self):
        return self._root

    def setRoot(self, data):
        newNode = DListNode(data)
        self._root = newNode

    def isEmpty(self):
        return self._root == None

    def insertFront(self, data):
        newNode = DListNode(data=data, next=self._root)
        if self._root:
            current = self._root
            current.setPrevNode(newNode)
        self.setRoot(newNode)

    def insertBack(self, data):
        newNode = DListNode(data=data)
        if not self._root:
            self.setRoot(newNode)
        else:
            current = self._root
            while current.getNextNode():
                current = current.getNextNode()
            current.setNextNode(newNode)
            newNode.setPrevNode(current)

    def exists(self, data):
        if not self._root:
            return False
        current = self._root
        while current and current.getData() != data:
            current = current.getNextNode()
        if current:
            return False
        else:
            return True

    def getNode(self, data):
        if not self._root:
            return None
        current = self._root
        while current and current.getData() != data:
            current = current.getNextNode()
        return current  # will be none if not found

    def delete(self, data):
        # if the DLLL is empty
        if not self._root:
            return False
        current = self._root
        while current and current.getData() != data:
            current = current.getNextNode()
        if not current:
            return False
        else:
            # if the current is the first node in DLLL
            if current is self._root:
                self.setRoot(current.getNextNode())
                # check whether the DLLL still has values to avoid an exception
                if not self._root:
                    self._root.setPrevNode(None)
            else:
                current.getPrevNode().setNextNode(current.getNextNode())
                # check whether the node is not None, to avoid an exception
                if current.getNextNode():
                    current.getNextNode().setPrevNode(current.getPrevNode())
            # the next two lines set the current node has no pointer-like things
            # not necessary as current is not accessible from the DLLL
            current.setPrevNode(None)
            current.setNextNode(None)
            return True

    def reverse(self):
        current = self._root
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
        if not self._root:
            return "Empty"
        else:
            result = ""
            current = self._root
            while current:
                result += str(current) + "\n"
                current = current.getNextNode()
            return result