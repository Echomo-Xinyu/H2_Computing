# this file is to implement a node-based Binary Search Tree with a tombstone in each node
import sys

class Node():
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right
        self._tombstone = False

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
        # return self._right
        self._right = Node
    
    def getTombstone(self):
        return self._tombstone
    
    def setTomestone(self, boo):
        self._tombstone = boo

    def __str__(self):
        #print(str(self.data)+str(self.left)+str(self.right))
        return "{0:<10}{1:<10}{2:<10}".format(
            (str(self._left.getValue()) if self._left else "None"),
            str(self._value) + ("(T)" if self._tombstone else ""),
            (str(self._right.getValue()) if self._right else "None"))


class BST():
    def __init__(self):
        self._root = None

    def isEmpty(self):
        return not self._root

    def insert(self, data):
        if not self._root:
            self._root = Node(data)
            return
        current = self._root
        while True:
            if current.getTombstone() and (
                    self.maxInSubTree(current.getLeft()) == None
                    or self.maxInSubTree(current.getLeft()) < data) and (
                        self.minInSubTree(current.getRight())
                        or self.minInSubTree(current.getRight()) >= data):
                current.setValue(data)
                # current.tombstone = False
                current.setTomestone(False)
                break
            elif data < current.getValue():
                if not current.getLeft():
                    current.setLeft(Node(data))
                    return
                else:
                    current = current.getLeft()
            else:
                if not current.getRight():
                    current.setRight(Node(data))
                    return
                else:
                    current = current.getRight()

    def findTarget(self, data):
        if not self._root:
            return None
        current = self._root
        while True:
            if data == current.getValue() and not current.getTombstone():
                # current._tombstone = True
                return current
            elif data < current.getValue():
                if not current.getLeft():
                    return None
                else:
                    current = current.getLeft()
            else:
                if not current.getRight():
                    return None
                else:
                    current = current.getRight()

    def exists(self, data):
        return self.findTarget(data) != None

    def delete(self, data):
        target = self.findTarget(data)
        if target:
            # target._tombstone = True
            target.setTomestone(True)
            return True
        return False

    def minInSubTree(self, node):
        if not node:
            return None
        if node.getTombstone():
            # res is a very large value, 2**63
            res = sys.maxsize
        else:
            res = node.getValue()
        # this part should add in extra check for the tombstone
        leftMin = self.minInSubTree(node.getLeft())
        rightMin = self.minInSubTree(node.getRight())
        # instead of not leftMin, but simply leftMin
        if leftMin:
            res = min(res, leftMin)
        if rightMin:
            res = min(res, rightMin)
        return res

    def maxInSubTree(self, node):
        if not node:
            return None
        if node.getTombstone():
            # res is assigned a very small value
            res = -sys.maxsize-1
        else:
            res = node.getValue()
        # print(node)
        # print(res)
        # this part should add in extra check for the tombstone
        leftMax = self.maxInSubTree(node.getLeft())
        rightMax = self.maxInSubTree(node.getRight())
        # print(leftMax)
        if leftMax:
            res = max(res, leftMax)
        # print(rightMax)
        if rightMax:
            res = max(res, rightMax)
        return res

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
            # print(current.getLeft())
            if current.getLeft():
                stack.append(current.getLeft())
            # print(current.getRight())
            if current.getRight():
                stack.append(current.getRight())
            # print(stack)

# a = BST()
# a.insert(5)
# a.insert(2)
# a.insert(7)
# a.print()
# a.insert(5.1)
# a.insert(8)
# if a.exists(2):
#     a.print()
#     a.delete(5)
#     a.print()
# if a.exists(10):
#     print("hey dude you got problem")
# a.insert(5.5)
# a.print()

# b = BST()
# b.insert(5)
# b.insert(2)
# b.insert(4.9)
# b.insert(7)
# if b.exists(5):
#     b.delete(5)
#     b.print()
# b.insert(4.8)
# b.print()

# c = BST()
# c.insert(1)
# c.insert(5)
# c.insert(2)
# c.insert(7)
# c.print()
# c.insert(5.1)
# c.insert(8)
# if c.exists(2):
#     c.print()
#     c.delete(5)
#     c.print()
# if c.exists(10):
#     print("hey dude you got problem")
# c.insert(5.5)
# c.print()

# d = BST()
# d.insert(1)
# d.insert(5)
# d.insert(2)
# d.insert(4.9)
# d.insert(7)
# if d.exists(5):
#     d.delete(5)
#     d.print()
# d.insert(4.8)
# d.print()

# e = BST()
# e.insert(1)
# e.insert(5)
# e.insert(2)
# e.insert(4.9)
# e.insert(7)
# if e.exists(5):
#     e.delete(5)
#     e.print()
# if e.exists(4.9):
#     e.delete(4.9)
#     e.print()
# e.insert(4.8)
# e.print()