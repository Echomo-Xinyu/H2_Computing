class queue():
    def __init__(self, capacity=2):
        # range: 0 <= self.head < self.capacity, same for self.rear
        # self.size is used to monitor the size of the queue
        self.head, self.size = 0, 0
        # such that frist time it will add to 0th index of array
        self.rear = capacity - 1
        self.capacity = capacity
        self.array = [None for i in range(capacity)]
    
    def isEmpty(self):
        return self.size <= 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, data):
        if self.isFull():
            # print error message
            return
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = data
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            # print error message
            return
        dataToDequeue = self.array[self.head]
        # erase the data stored at the dequeued position, not necessary
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return dataToDequeue
    
    def front(self):
        # will return None if is empty
        return self.array[self.head]
    
    def end(self):
        # return None if empty
        return self.array[self.rear]
    
    def print(self):
        if self.isEmpty():
            return "Empty"
        result = str(self.array[self.head])
        index = self.head + 1
        # print("head " + str(self.head))
        for index in range(1, self.size):
            index = (index + self.head) % self.capacity
            result += " -> " + str(self.array[index])
        print(result)
        # print(self.array)

a = queue(5)
a.enqueue(1)
a.print()
print(a.front())
print(a.end())
print(a.dequeue())
a.print()
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.print()
a.enqueue(5)
a.enqueue(6)
a.print()
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
a.enqueue(1)
a.enqueue(7)
a.print()