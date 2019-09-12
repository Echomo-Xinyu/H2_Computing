# the file is to write a typical version of Binary Search Tree
class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return "{0:10}{1:10}{2:10}".format(str(self.left.data) if self.left else "None", str(self.data), str(self.right.data) if self.right else "None")

class BST():
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root == None:
            self.root = Node(data=data)
            return
        self.insertR(data, self.root)
    def insertR(self, data, current):
        if data < current.data:
            if current.left == None:
                current.left = Node(data)
                return
            else:
                self.insertR(data, current.left)
        
        else:
            if current.right == None:
                current.right = Node(data)
                return
            else:
                self.insertR(data, current.right)
    def insertI(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        newNode = Node(data)
        currentNode = self.root
        while True:
            if data < currentNode.data:
                if currentNode.left == None:
                    currentNode.left = newNode
                    return
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right == None:
                    currentNode.right = newNode
                    return
                else:
                    currentNode = currentNode.right
    
    def exists(self, data):
        if self.root == None:
            return False
        return self.existsR(data, self.root)
    def existsR(self, data, current):
        if data == current.data:
            return True
        elif data < current.data:
            if current.left == None:
                return False
            else:
                return self.existsR(data, current.left)
        else:
            if current.right == None:
                return False
            else:
                return self.existsR(data, current.right)
    def existsI(self, data):
        if self.root == None:
            return False
        currentNode = self.root
        while True:
            if data == currentNode.data:
                return True
            if data < currentNode.data:
                if currentNode.left == None:
                    return False
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right == None:
                    return False
                else:
                    currentNode = currentNode.right
    
    def inOrderTraversal(self, current):
        result = []
        if current:
            # check use of self function call
            result += self.inOrderTraversal(current.left)
            result.append(current)
            result += self.inOrderTraversal(current.right)
        return result

    def preOrderTraversal(self, current):
        result = []
        if current:
            result.append(current)
            result += self.preOrderTraversal(current.left)
            result += self.preOrderTraversal(current.right)
        return result

    def postOrderTraversal(self, current):
        result = []
        if current:
            result += self.postOrderTraversal(current.left)
            result += self.postOrderTraversal(current.right)
            result.append(current)
        return result
    
    def print(self):
        if self.root == None:
            print("Empty BST")
            return
        print("{0:10}{1:10}{2:10}".format("left", "data", "right"))
        lis = self.inOrderTraversal(self.root)
        for i in range(len(lis)):
            print(str(lis[i]))

a = BST()
a.insert(5)
a.insert(2)
a.insert(7)
a.print()
a.insert(5.1)
a.insert(8)
if a.exists(2):
    a.print()
if a.exists(10):
    print("hey dude you got problem")
a.insert(5.5)
a.print()

print("------------------", end="\n\n\n")

b = BST()
b.insertI(10)
b.insertI(2)
b.insert(17)
b.print()
b.insertI(34)
b.print()
if b.existsI(34):
    print("hey man")

        











