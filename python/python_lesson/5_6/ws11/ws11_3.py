class Node():
    def __init__(self, data=None, left=-1, right=-1):
        self.Data = data
        self.LeftP = left
        self.RightP = right


ThisTree = [Node() for i in range(20)]

for i in range(0, 20):
    ThisTree[i].LeftP = i + 1
    # print(ThisTree[i].LeftP)

class BST():
    def __init__(self):
        self.Root, self.NextFreePosition = -1, 0

    def AddItemToBinaryTree(self, NewFreeItem):
        if self.Root == -1:
            self.Root = self.NextFreePosition
            ThisTree[self.Root].Data = NewFreeItem
            self.NextFreePosition = ThisTree[self.Root].LeftP
        elif self.NextFreePosition == 20:
            print("Fail to add the item for the tree is full")
            return
        else:
            CurrentPosition = self.Root
            LastMove = "X"
            while CurrentPosition != -1:
                PreviousPosition = CurrentPosition
                if NewFreeItem < ThisTree[CurrentPosition].Data:
                    LastMove = "L"
                    CurrentPosition = ThisTree[CurrentPosition].LeftP
                else:
                    LastMove = "R"
                    CurrentPosition = ThisTree[CurrentPosition].RightP
            if LastMove == "R":
                ThisTree[PreviousPosition].RightP = self.NextFreePosition
            else:
                ThisTree[PreviousPosition].LeftP = self.NextFreePosition
            ThisTree[self.NextFreePosition] = NewFreeItem
            print("NFP: ", self.NextFreePosition)
            print("THIS TREE[NFP]: ", ThisTree[self.NextFreePosition].LeftP)
            self.NextFreePosition = ThisTree[self.NextFreePosition].LeftP
            ThisTree[self.NextFreePosition - 1].LeftP = 0
    
    def OutputData(self):
        print(self.Root)
        print(self.NextFreePosition)
        for i in range(self.Root, self.NextFreePosition):
            print(str(ThisTree[i].LeftP)+" "+str(ThisTree[i].Data)+" "+str(ThisTree[i].RightP))

BST_1 = BST()
while True:
    input_value = input()
    if input_value == "XXX":
        break
    else:
        BST_1.AddItemToBinaryTree(input_value)