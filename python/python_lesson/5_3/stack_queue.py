# the file is to implement an array-based stack and queue
class stack():
    def __init__(self, size=1):
        # self.top indicates the index of last element of the stack
        # thus the -1 <= self.top <= self.size - 1
        self.top = -1
        self.size = size # or use len(self.array) in real practice
        self.array = [None for i in range(size)]
    
    def isEmpty(self):
        return self.top < 0
    
    def isFull(self):
        return self.size - 1 == self.top
    
    # if not return value, print an error message when return False
    def push(self, data):
        if self.isFull():
            return False
        else:
            self.top += 1
            self.array[self.top] = data
            return True
    
    # if not return value, print an error message when return False
    def pop(self):
        if self.isEmpty():
            return None
        else:
            toPop = self.array[self.top]
            # not nexessary to erase
            self.array[self.top] = None
            self.top -= 1
            return toPop

class queue():
    def __init__(self, size=1):
        # range: -1 <= self.head < self.size
        # same for self.tail
        self.head = -1
        self.tail = 0
        self.size = size # same as stack, can choose not to keep
        self.array = [None for i in range(size)]
    
    def isEmpty(self):
        # in dequeue, if empty, the self.head will be reset to -1
        # once enqueue any element, change self.head to 0
        return self.head < 0
    
    def isFull(self):
        return self.head == self.tail
    
    def enqueue(self, data):
        if self.isFull():
            return False
        self.array[self.tail] = data
        if self.tail + 1 == self.size:
            # move to front if at the end of the array container
            self.tail = 0
        else:
            self.tail += 1
        # if add in first element, initialize self.head
        if self.head < 0:
            self.head = 0
        return True
    
    def dequeue(self):
        if self.isEmpty():
            # print error message
            return None
        toDequeue = self.array[self.head]
        if self.head + 1 == self.size:
            self.head = 0
        else:
            self.head += 1
        self.array[self.head] = None
        # reset the queue once empty
        if self.tail == self.head:
            self.tail, self.head = 0, -1
        return toDequeue
    
    def peek(self):
        return self.array[self.head]
    
    def print(self):
        if self.isEmpty():
            return "Empty"
        result = str(self.array[self.head+1])
        index = self.head+1
        print("head " + str(self.head))
        while (index != self.tail and self.array[index] != None):
            result += " -> " + str(self.array[index])
            if index+1 == self.size:
                index = 0
            else:
                index += 1
        print(result)

    

a = queue(10)
a.enqueue(1)
a.print()
a.dequeue()
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
a.enqueue(2)
print(a.enqueue(2))
a.dequeue()
a.print()
a.dequeue()
a.dequeue()
a.print()
a.dequeue()
a.dequeue()
a.print()
a.dequeue()