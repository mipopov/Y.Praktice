#15 авг 2020, 20:21:12 ID - 33776783
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[- 1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.size = 0

    def getSize(self):
        return self.size

    def push(self, elem):
        self.stack1.push(elem)
        self.size += 1

    def pop(self):
        self.size -= 1
        if self.stack2.size() == 0:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()


n = int(input())
i = 0
newQueue = Queue()

while i < n:
    inputStr = input().split()
    operation = inputStr[0]
    if operation == "put":
        newQueue.push(int(inputStr[1]))
    elif operation == "get":
        if newQueue.getSize() == 0:
            print("error")
        else:
            print(newQueue.pop())
    elif operation == "get_size":
        print(newQueue.getSize())
    i += 1

