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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class StackSet:
    def __init__(self):
        self.stackSet = set()
        self.elem = Stack()

    def push(self, item):
        if item not in self.stackSet:
            self.elem.push(item)
            self.stackSet.add(item)

    def pop(self):
        self.stackSet.remove(self.elem.pop())

    def size(self):
        return len(self.stackSet)

    def peek(self):
        return self.elem.peek()

n = int(input())

i = 0
newStack = StackSet()
while i < n:
    inputStr = input().split()
    operation = inputStr[0]
    if operation == "push":
        newStack.push(int(inputStr[1]))
    elif operation == "pop":
        if newStack.size() == 0:
            print("error")
        else:
            newStack.pop()
    elif operation == "peek":
        if newStack.size() == 0:
            print("error")
        else:
            print(newStack.peek())
    elif operation == "size":
        print(newStack.size())
    i += 1