# this file is to implement a node-based Binary Search Tree
class Node():
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def getValue(self):
        return self._value

    def setValue(self, data):
        self._value = data

    def getLeft(self):
        return self._left

    def setLeft(self, Node):
        self._left = Node

    def getRight(self):
        return self._right

    def setRight(self, Node):
        return self._right

    def __str__(self):
        #print(str(self.data)+str(self.left)+str(self.right))
        return "{0:<10}{1:<10}{2:<10}".format(self._value, self._left,
                                              self._right)


class BST():
    def __init__(self):
        self._root = None

    def isEmpty(self):
        return not self._root

    def insert(self, data):
        newNode = Node(data)
        # if it is empty
        if self.isEmpty():
            self._root = newNode
            return
        current = self._root
        while True:
            if data <= current.getValue():
                if not current.getLeft():
                    current = current.getLeft()
                else:
                    current.setLeft(newNode)
                    return
            else:
                if not current.getRight():
                    current = current.getRight()
                else:
                    current.setRight(newNode)
                    return

    def exist(self, data):
        if self.isEmpty():
            return False
        current = self._root
        while current:
            if data == current.getValue():
                return True
            elif data < current.getValue():
                current = current.getLeft()
            else:  # data > current.getValue():
                current = current.getRight()
        return False

    def print(self):
        if self.isEmpty():
            print("Empty")
            return
        stack = [self._root]
        print("{0:<10}{1:<10}{2:<10}".format("Node.data", "Node.left",
                                             "Node.right"))
        while len(stack) > 0:
            current = stack.pop()
            print(current)
            if current.getLeft():
                stack.append(current.getLeft())
            if current.getRight():
                stack.append(current.getRight())
