#7 авг 2020, 20:29:55 - ID - 33746938
# Реализация Стэк
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
# Реализация очереди на 6 стэках
class Queue:
    def __init__(self):
        self.leftStack = Stack()
        self.rightStack = Stack()
        self.leftStack_help_push = Stack()
        self.rightStack_copy = Stack()
        self.rightStack_copy_copy = Stack()
        self.helperStackS = Stack()
        self.size = 0
        self.recopy = False
        self.copied = False
        self.toCopy = 0

    def isEmpty(self):
        return self.recopy == False and self.rightStack.size() == 0

    def getSize(self):
        return self.size

    def push(self, newItem):
        self.size += 1
        if self.recopy:
            self.leftStack_help_push.push(newItem)
            self.checkNormal()
        else:
            self.leftStack.push(newItem)
            if self.rightStack_copy_copy.size() > 0:
                self.rightStack_copy_copy.pop()
            self.checkRecopy()

    def pop(self):
        self.size -= 1
        if self.recopy:
            tmp = self.rightStack_copy.pop()
            if self.toCopy > 0:
                self.toCopy -= 1
            else:
                self.rightStack.pop()
                self.rightStack_copy_copy.pop()
            self.checkNormal()
            return tmp
        else:
            tmp = self.rightStack.pop()
            self.rightStack_copy.pop()
            if self.rightStack_copy_copy.size() > 0:
                self.rightStack_copy_copy.pop()
            self.checkRecopy()
            return tmp

    # Нужно ли начинать перекопирование
    def checkRecopy(self):
        self.recopy = self.leftStack.size() > self.rightStack.size()
        if self.recopy:
            self.toCopy = self.rightStack.size()
            self.copied = False
            self.checkNormal()

    def checkNormal(self):
        self.additionalOperations()
        self.recopy = self.helperStackS.size() > 0

    # Происходит перекопирование элементов
    def additionalOperations(self):
        toDo = 3
        while self.copied == False and toDo > 0 and self.rightStack.size() > 0:
            self.helperStackS.push(self.rightStack.pop())
            toDo -= 1
        while toDo > 0 and self.leftStack.size() > 0:
            self.copied = True
            elem = self.leftStack.pop()
            self.rightStack.push(elem)
            self.rightStack_copy_copy.push(elem)
            toDo -= 1

        while toDo > 0 and self.helperStackS.size() > 0:
            elem = self.helperStackS.pop()
            if self.toCopy > 0:
                self.rightStack.push(elem)
                self.rightStack_copy_copy.push(elem)
                self.toCopy -= 1
            toDo -= 1

        if self.helperStackS.size() == 0:
            self.leftStack, self.leftStack_help_push = self.leftStack_help_push, self.leftStack
            self.rightStack_copy, self.rightStack_copy_copy = self.rightStack_copy_copy, self.rightStack_copy


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









