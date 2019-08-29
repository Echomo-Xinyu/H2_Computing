class SNode():
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class SLLL():
    def __init__(self, root=None):
        self.root = root
    
    def insertFront(self, data):
        newNode = SNode(data)
        if self.root == None:
            self.root = newNode
            return
        newNode.next = self.root
        self.root = newNode
        return
    
    def insertBack(self, data):
        newNode = SNode(data)
        if self.root == None:
            self.root = newNode
            return
        currentNode = self.root
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode
    
    def exists(self, data):
        if self.root == None:
            return False
        currentNode = self.root
        while currentNode and currentNode.data != data:
            currentNode = currentNode.next
        if not currentNode:
            return False
        return True
    
    def insertInOrder(self, data):
        newNode = SNode(data)
        # one node
        if self.root == None:
            self.root = SNode(data)
            return
        # smaller than the first
        if self.root.data > data:
            self.insertFront(data)
            # print("hey")
            return
        prevNode, currentNode = self.root, self.root.next
        while currentNode:
            if prevNode.data <= data and data < currentNode.data:
                prevNode.next = newNode
                newNode.next = currentNode
                return
            prevNode, currentNode = currentNode, currentNode.next
        prevNode.next = newNode
    
    def delete(self, data):
        if self.root == None:
            return False
        if self.root.data == data:
            self.root = self.root.next
            return True
        currentNode = self.root
        while currentNode.next and currentNode.next.data != data:
            currentNode = currentNode.next
        if not currentNode.next:
            return False
        else:
            currentNode.next = currentNode.next.next
            return True


    def print(self):
        if self.root == None:
            print("Empty")
            return
        result = ""
        currentNode = self.root
        while currentNode:
            result += str(currentNode) + ", "
            currentNode = currentNode.next
        print(result)

a = SLLL()
a.insertBack(1)
a.insertBack(7)
a.insertBack(4)
a.print()

b = SLLL()
b.insertInOrder(1)
b.insertInOrder(-1)
b.insertInOrder(0)
b.print()

c = SLLL()
c.insertFront(0)
c.insertFront(-1)
c.insertFront(5)
c.print()

d = SLLL()
d.insertFront(0)
d.delete(0)
d.print()
d.insertBack(10)
d.insertBack(12)
d.print()
d.delete(10)
d.delete(9)
d.print()

class DNode(SNode):
    def __init__(self, data=None):
        super().__init__(data=data)
        self.prev = None
    def __str__(self):
        return super().__str__()

class DLLL(SLLL):
    def __init__(self, root=None):
        super().__init__(root=root)
    def insertFront(self, data):
        newNode = DNode(data)
        if self.root == None:
            self.root = newNode
            return
        newNode.next, self.root.prev = self.root, newNode
        self.root = newNode
    def insertBack(self, data):
        newNode = DNode(data)
        if self.root == None:
            self.root = newNode
            return
        currentNode = self.root
        while currentNode.next:
            currentNode = currentNode.next
        newNode.prev, currentNode.next = currentNode, newNode
    def exsits(self, data):
        return super().exists(data)
    def insertInOrder(self, data):
        newNode = DNode(data)
        if self.root == None:
            self.root  = newNode
            return
        if self.root.data > data:
            self.insertFront(data)
            return
        currentNode = self.root
        while currentNode.next:
            if currentNode.data <= data and data < currentNode.next.data:
                currentNode.next.prev, newNode.next = newNode, currentNode.next
                currentNode.next, newNode.prev = newNode, currentNode
                return
            currentNode = currentNode.next
        currentNode.next, newNode.prev = newNode, currentNode
    def delete(self, data):
        if self.root == None:
            return False
        if self.root.data == data:
            self.root = self.root.next
            if self.root:
                self.root.prev = None
            return True
        currentNode = self.root
        while currentNode.next and currentNode.next.data != data:
            currentNode = currentNode.next
        if not currentNode.next:
            return False
        currentNode.next = currentNode.next.next
        if currentNode.next:
            currentNode.next.prev = currentNode
        # currentNode.next, currentNode.prev = None, None
        return True

e = DLLL()
e.insertFront(0)
e.insertFront(1)
e.insertFront(10)
e.print()
e.delete(5)
e.delete(1)
e.print()
e.delete(0)
e.delete(10)

f = DLLL()
f.insertInOrder(-2)
f.insertInOrder(98)
f.insertInOrder(10)
f.print()
f.delete(10)
f.print()
f.insertInOrder(-20)
f.print()
            
                

        