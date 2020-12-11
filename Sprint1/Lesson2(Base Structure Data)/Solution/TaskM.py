class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)] 
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def isEmty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def put(self, elem):
        if self.size != self.max_n:
            self.queue[self.tail] = elem
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return "error"
    def peek(self):
        if self.isEmty():
            return None
        return self.queue[self.head]

    def pop(self):
        if self.isEmty():
            return None
        elem = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return elem


n = int(input())

i = 0
newQueue = MyQueue(n)
while i < n:
    inputStr = input().split()
    operation = inputStr[0]
    if operation == "push":
        newQueue.put(int(inputStr[1]))
    elif operation == "pop":
            print(newQueue.pop())
    elif operation == "peek":
        print(newQueue.peek())
    elif operation == "size":
        print(newQueue.getSize())
    i += 1