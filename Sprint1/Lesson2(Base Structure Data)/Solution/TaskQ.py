class Dequeue:
    def __init__(self, maxSize):
        self.deq = [None for _ in range(maxSize)]
        self.head = 0
        self.tail = 0
        self.max_n = maxSize
        self.size = 0

    def push_back(self, elem):
        if self.size == self.max_n:
            print("error")
        else:
            self.deq[self.tail] = elem
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop_back(self):
        if self.size == 0:
            return "error"
        else:
            self.tail = (self.tail - 1) % self.max_n
            self.size -= 1
            return self.deq[self.tail]

    def push_front(self, elem):
        if self.size == self.max_n:
            print("error")
        else:
            self.head = (self.head - 1) % self.max_n
            self.deq[self.head] = elem
            self.size += 1

    def pop_front(self):
        if self.size == 0:
            return "error"
        else:
            elem = self.deq[self.head]
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            return elem

n = int(input())
maxN = int(input())
i = 0
newQueue = Dequeue(maxN)

while i < n:
    inputStr = input().split()
    operation = inputStr[0]
    if operation == "push_back":
        newQueue.push_back(int(inputStr[1]))
    elif operation == "push_front":
        newQueue.push_front(int(inputStr[1]))
    elif operation == "pop_front":
        print(newQueue.pop_front())
    elif operation == "pop_back":
        print(newQueue.pop_back())

    i += 1




