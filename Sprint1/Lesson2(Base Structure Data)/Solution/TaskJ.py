class StackEffectMax:
    def __init__(self):
        self.items = []
        self.maxItems = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty() or item >= self.getMax():
            self.maxItems.append(item)
        self.items.append(item)

    def pop(self):
        value = self.items.pop()
        if value == self.getMax():
            self.maxItems.pop()
        return value

    def getMax(self):
        return self.maxItems[-1]

n = int(input())
i = 0
newStack = StackEffectMax()
while i < n:
    inputStr = input().split()
    operation = inputStr[0]
    if operation == "push":
        newStack.push(int(inputStr[1]))
    elif operation == "pop":
        if newStack.isEmpty():
            print("error")
        else:
            newStack.pop()
    elif operation == "get_max":
        if newStack.isEmpty():
            print("None")
        else:
            print(newStack.getMax())

    i += 1


