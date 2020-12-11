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

class StackMax:
    def __init__(self):
        self.stack = Stack()

    def getMax(self):
        return max(self.stack.items)

n = int(input())

i = 0
newStack = StackMax()
while i < n:
    inputStr = input().split()
    operation = inputStr[0]
    if operation == "push":
        newStack.stack.push(int(inputStr[1]))
    elif operation == "pop":
        if newStack.stack.size() == 0:
            print("error")
        else:
            newStack.stack.pop()
    elif operation == "get_max":
        if newStack.stack.size() == 0:
            print("None")
        else:
            print(newStack.getMax())
    i += 1