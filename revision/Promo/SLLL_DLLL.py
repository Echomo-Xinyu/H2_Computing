# the file is a revision for SLLL and DLLL
class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.data)

class SLLL():
    def __init__(self):
        self.root = None
    def insertFront(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            newNode.next = self.root
            self.root = newNode
    def insertBack(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
    def delete(self, data):
        if self.root == None:
            return False
        if self.root.data == data:
            self.root = self.root.next
            return True
        currentNode = self.root
        while currentNode.next != None and currentNode.next.data != data and currentNode.next.next!=None:
            currentNode = currentNode.next
        if currentNode.next != None:
            currentNode.next = currentNode.next.next
            return True
        else:
            return False
    def exists(self, data):
        if self.root == None:
            return False
        currentNode = Node(data)
        while currentNode.data != data and currentNode.next != None:
            currentNode = currentNode.next
        if currentNode.data == data:
            return True
        else:
            return False
    # the function is under the assumption that the SLLL is in order by nature
    def insertInOrder(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
            return
        if self.root.data >= data:
            newNode.next = self.root
            self.root = newNode
            return
        currentNode = self.root
        while currentNode.next and currentNode.next.data < data:
            currentNode = currentNode.next
        if currentNode.next == None:
            currentNode.next = newNode
            return
        else:
            newNode.next = currentNode.next
            currentNode.next = newNode
            return
    def print(self):
        if self.root == None:
            print("Empty")
        else:
            currentNode = self.root
            while currentNode:
                print(str(currentNode), end=", ")
                currentNode = currentNode.next
            print("")
            return

a = SLLL()
a.insertFront(1)
a.print()
a.insertFront(2)
a.insertFront(10)
a.print()
a.insertBack(5)
a.print()
a.delete(10)
a.print()
a.delete(1)
a.print()

b = SLLL()
b.insertInOrder(1)
b.print()
b.insertInOrder(-1)
b.print()
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

class DLLL(SLLL):
    def __init__(self):
        # self.root = None
        super.__init__(self)
    def insertFront(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            newNode.next = self.root
            # missing point
            self.root.prev = newNode
            self.root = newNode
    def insertBack(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = Node(data)
        else:
            currentNode = self.root
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode
    def exists(self, data):
        if self.root == None:
            return False
        currentNode = self.root
        while currentNode.data != data and currentNode.next:
            currentNode = currentNode.next
        if currentNode.data == data:
            return True
        else:
            return False
    def delete(self, data):
        if self.root == None:
            return False
        if self.root.data == data:
            self.root = self.root.next
            # missing condition check
            if self.root != None:
                self.root.prev = None
            return True
        currentNode = self.root
        while currentNode.next and currentNode.next.data != data:
            currentNode = currentNode.next
        if currentNode.next == None:
            return False
        else:
            currentNode.next = currentNode.next.next
            # missing condition check
            if currentNode.next != None:
                currentNode.next.prev = currentNode
            return True
    # this function assumes all the Nodes in DLLL are sorted
    def insertInOrder(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        if self.root.data >= data:
            self.insertFront(data)
            return
        currentNode = self.root
        # the loop break when at the end
        while currentNode.next:
            # if the data should be inserted during loop
            if currentNode.data <= data and data <= currentNode.next.data:
                newNode = Node(data=data, next=currentNode.next, prev=currentNode)
                currentNode.next.prev = newNode
                currentNode.next = newNode
                return
        newNode = Node(data=data, prev=currentNode)
        currentNode.next = newNode

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
            


            
