# update on 22 May: complete implementing the thing and pass the test case
class Node():
    def __init__(self, data=None, left=-1, right=-1):
        self.Data = data
        self.LeftP = left
        self.RightP = right


ThisTree = [Node(data=None) for i in range(20)]
# print(type(ThisTree))
# print(type(ThisTree[0]))
# <class 'list'>
# <class '__main__.Node'>

for i in range(0, 20):
    ThisTree[i].LeftP = i + 1
    # print(ThisTree[i].LeftP)
ThisTree[19].LeftP = -1

# for i in range(20):
#     print(ThisTree[i].LeftP)


class BST():
    def __init__(self):
        self.Root = -1
        self.NextFreePosition = 0

    def AddItemToBinaryTree(self, NewFreeItem):
        # print(type(ThisTree[0]))
        if self.Root == -1:
            # print("Block of code executed")
            self.Root = self.NextFreePosition
            ThisTree[self.Root].Data = NewFreeItem
            self.NextFreePosition = ThisTree[self.Root].LeftP
            ThisTree[self.Root].LeftP = -1
        elif self.NextFreePosition == 20:
            print("Fail to add the item for the tree is full")
            return
        else:
            # print("He")
            CurrentPosition = self.Root
            LastMove = "X"
            while CurrentPosition != -1:
                PreviousPosition = CurrentPosition
                # try:
                # print(type(NewFreeItem), type(ThisTree[CurrentPosition].Data))
                # print(CurrentPosition)
                if NewFreeItem < ThisTree[CurrentPosition].Data:
                    LastMove = "L"
                    CurrentPosition = ThisTree[CurrentPosition].LeftP
                else:
                    LastMove = "R"
                    CurrentPosition = ThisTree[CurrentPosition].RightP
                    # except:
                    #     print("Type of newFreeItem", type(NewFreeItem))
                    #     print("Type of TT[CP].Data", type(ThisTree[CurrentPosition].Data))
            if LastMove == "R":
                ThisTree[PreviousPosition].RightP = self.NextFreePosition
            else:
                ThisTree[PreviousPosition].LeftP = self.NextFreePosition
            ThisTree[self.NextFreePosition].Data = NewFreeItem
            # print("NFP: ", self.NextFreePosition)
            # print(type(self.NextFreePosition))
            # print(type(ThisTree[0]))
            # print(type(ThisTree[self.NextFreePosition]))
            # print("THIS TREE[NFP]: ", ThisTree[self.NextFreePosition].LeftP)
            self.NextFreePosition = ThisTree[self.NextFreePosition].LeftP
            ThisTree[self.NextFreePosition-1].LeftP = -1

    def OutputData(self):
        if self.Root == -1:
            print("Empty")
        else:
            # print("Root: ", self.Root)
            # print("NFP: ", self.NextFreePosition)
            for i in range(self.Root, self.NextFreePosition):
                print(
                    str(ThisTree[i].LeftP) + " " + str(ThisTree[i].Data) +
                    " " + str(ThisTree[i].RightP))


BST_1 = BST()
while True:
    input_value = input()
    if input_value == "XXX":
        break
    else:
        # BST_1.OutputData()
        BST_1.AddItemToBinaryTree(input_value)
        BST_1.OutputData()

def inOrderTraversal(current):
    if current!=-1:
        inOrderTraversal(ThisTree[current].LeftP)
        print(ThisTree[current].Data)
        inOrderTraversal(ThisTree[current].RightP)

inOrderTraversal(0)