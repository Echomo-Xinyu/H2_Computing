# # Q3
# class Node():
#     def __init__(self, data, leftPtr=None, rightPtr=None):
#         self.data = data
#         self.leftPtr = leftPtr
#         self.rightPtr = rightPtr

#     def setData(self, data):
#         self.data = data

#     def setLeftPtr(self, pointer):
#         self.leftPtr = pointer

#     def setRightPtr(self, pointer):
#         self.rightPtr = pointer

#     def getData(self):
#         return self.data

#     def getLeftPtr(self):
#         return self.leftPtr

#     def getRightPtr(self):
#         return self.rightPtr


# class ADT():
#     def __init__(self):
#         self.tree = []
#         self.root = -1

#     def add(self, data):
#         self.tree.append(Node(data))
#         if self.root == -1:
#             self.root = 0
#             return
#         # locate the position to insert the node and its parent node
#         last_node_left = True
#         current = self.root
#         while current != None:
#             previous_node = current
#             if self.tree[current].getData() < data:
#                 current = self.tree[current].getLeftPtr()
#                 last_node_left = True
#             else:
#                 current = self.tree[current].getRightPtr()
#                 last_node_left = False
#         # insert to left or right based on link with its parent node
#         if last_node_left:
#             self.tree[previous_node].setLeftPtr(len(self.tree))
#         else:
#             self.tree[previous_node].setRightPtr(len(self.tree))

#     def print(self):
#         n = len(self.tree)
#         print("{0:10};{1:15};{2:15}".format("Data", "LeftPointer",
#                                             "RightPointer"))
#         for i in range(n):
#             print("{0:10};{1:15};{2:15}".format(
#                 self.tree[i].getData(), self.tree[i].getLeftPtr()
#                 if self.tree[i].getLeftPtr() else "           None",
#                 self.tree[i].getRightPtr()
#                 if self.tree[i].getRightPtr() else "           None"))

#     def _iOTr(self, current):
#         if current != None:
#             self._iOTr(self.tree[current].getLeftPtr())
#             print("{0:10}".format(
#                 self.tree[current].getData())
#             self._iOTr(self.tree[current].getRightPtr())

#     def inOrderTraversal(self):
#         if self.root == -1:
#             print("Empty")
#             # return
#         self._iOTr(self.root)


# a = ADT()
# a.add("Dave")
# a.add("Fred")
# a.add("Ed")
# a.add("Greg")
# a.add("Bob")
# a.add("Cid")
# a.add("Ali")
# a.print()
# a.inOrderTraversal()