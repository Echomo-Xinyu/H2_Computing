# the file is a practice to write a array-based stack and queue from scratch
class stack():
    def __init__(self, size=10):
        self.size = size
        self.array = [None for i in range(size)]
        self.top = -1
    def isFull(self):
        return self.top + 1 == self.size
    def isEmpty(self):
        return self.top == -1
    def push(self, data):
        if self.isFull():
            print("The stack is full")
            return False
        self.top += 1
        self.array[self.top] = data
        return True
    def pop(self):
        if self.isEmpty():
            print("The stack is empty")
            return None
        toPop = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        return toPop
    def print(self):
        if self.isEmpty():
            print("Empty stack")
        result = ""
        for i in range(self.top+1):
            result += str(self.array[i]) + " -> "
        print(result[:-3])

class queue():
    def __init__(self, size=10):
        self.size = size
        self.array = [None for i in range(size)]
        self.head, self.tail = 0, 0
    # check based on whether the tail element is empty
    # usually the tail element should be empty
    def isFull(self):
        return self.tail == self.head and self.array[self.tail] != None
    def isEmpty(self):
        return self.head == self.tail and self.array[self.tail] == None
    def enqueue(self, data):
        if self.isFull():
            print("The queue is full")
            return False
        self.array[self.tail] = data
        self.tail = (self.tail + 1) % self.size
        return True
    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
            return None
        toPop = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.size
        return toPop
    def front(self):
        return self.array[self.head]
    def end(self):
        if self.tail == 0:
            return self.array[self.size-1]
        return self.array[self.tail-1]
    def print(self):
        if self.isEmpty():
            print("Empty queue")
        result = ""
        if self.head < self.tail:
            for i in range(self.head, self.tail):
                result += str(self.array[i]) + " -> "
            print(result[:-3])
            return
        else:
            for i in range(self.head, self.size):
                result += str(self.array[i]) + " -> "
            for i in range(self.tail):
                result += str(self.array[i]) + " -> "
            print(result[:-3])

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
a.enqueue(1)
a.enqueue(7)
a.print()
print(a.dequeue())

b = stack(5)
b.push(1)
b.print()
b.push(10)
b.push(56)
b.print()
print(b.pop())
b.print()
