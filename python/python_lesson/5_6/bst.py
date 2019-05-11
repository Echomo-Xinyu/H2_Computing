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

    def _str_(self):
        return "{0:<10}{1:<10}{2:<10}".format(
            (str(self._left.getValue()) if self._left else "None"),
            str(self._value),
            (str(self._right.getValue()) if self._right else "None"))


class BST():
    def __init__(self):
        self._root = None

    def isEmpty(self):
        return not self._root

    # wrap up methof for insertRecursive
    def insertR(self, data):
        if not self._root:
            self._root = Node(data)
        else:
            self.insertRecursive(data, self._root)

    def insertRecursive(self, data, current):
        if data < current.getValue():
            if not current.getLeft():
                current.setLeft(Node(data))
                # return
            else:
                self.insertRecursive(data, current.getLeft())
        else:
            if not current.getRight():
                current.setRight(Node(data))
            else:
                self.insertRecursive(data, current.getRight())

    def insertIterative(self, data):
        newNode = Node(data)
        # if it is empty
        if self.isEmpty():
            self._root = newNode
            return
        current = self._root
        while True:
            if data < current.getValue():
                if not current.getLeft():
                    current = current.getLeft()
                else:
                    current.setLeft(newNode)
                    return
            else:  # elif data > current.getValue():
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

    def existR(self, data):
        if self.isEmpty():
            return False
        else:
            self.existRecursive(data, self._root)

    def existRecursive(self, data, current):
        if data == current.getValue():
            return True
        elif data < current.getValue():
            if not current.getLeft():
                return False
            else:
                return self.existRecursive(data, current.getLeft())
        else:
            if not current.getRight():
                return False
            else:
                return self.existRecursive(data, current.getRight())

    def print(self):
        # traverse from top to its right subtree then left for every node
        if self.isEmpty():
            print("Empty")
            return
        stack = [self._root]
        print("{0:<10}{1:<10}{2:<10}".format("Node.left", "Node.data",
                                             "Node.right"))
        while len(stack) > 0:
            current = stack.pop()
            print(current)
            if current.getLeft():
                stack.append(current.getLeft())
            if current.getRight():
                stack.append(current.getRight())

    # traverse the nodes in a seuqence such that the nodes can form the same tree
    # with the same sequence
    def pre_order_traversal(self, current):
        res = []
        if current:
            res.append(current.getValue())
            res += self.pre_order_traversal(current.getLeft())
            res += self.pre_order_traversal(current.getRight())
        return res

    # traverse the nodes in a sorted manner
    def in_order_traversal(self, current):
        res = []
        if current:
            res += self.in_order_traversal(current.getLeft())
            res.append(current)
            res += self.in_order_traversal(current.getRight())
        return res

    # traverse the nodes from bottom level, from left to right
    def post_order_traversal(self, current):
        res = []
        if current:
            res += self.post_order_traversal(current.getLeft())
            res += self.post_order_traversal(current.getRight())
            res.append(current)
        return res
