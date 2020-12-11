class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

class QueueNode:
    def __init__(self):
        self.tail = Node(None)
        self.head = Node(None)
        self.size = 0

    def getSize(self):
        return self.size

    def put(self, elem):
        newNode = Node(elem)
        newNode.next_item = None

        if self.getSize() == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next_item = newNode
            self.tail = newNode
        self.size += 1

    def get(self):
        if self.getSize() != 0:
            delNode = self.head
            print(self.head.value)
            self.head = self.head.next_item
            self.size -= 1
            del delNode
        else:
            print("error")

n = int(input())

i = 0
newQueue = QueueNode()
while i < n:
    inputStr = input().split()
    operation = inputStr[0]
    if operation == "put":
        newQueue.put(int(inputStr[1]))
    elif operation == "get":
            newQueue.get()
    elif operation == "size":
        print(newQueue.getSize())
    i += 1