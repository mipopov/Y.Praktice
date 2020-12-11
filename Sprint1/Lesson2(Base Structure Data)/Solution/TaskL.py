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
        if len(self.items) != 0:
            return self.items[len(self.items) - 1]
        else:
            return None

    def size(self):
        return len(self.items)

seqStack = Stack()
def is_correct_bracket_seq(seqStr):
    for i in seqStr:
        if (i == ")" and seqStack.peek() == "(") or (i == "]" and seqStack.peek() == "[") or (i == "}" and seqStack.peek() == "{"):
            seqStack.pop()
        elif i == ")" or i == "]" or i == "}":
            return False
        else:
            seqStack.push(i)
    return seqStack.isEmpty()

inputStr = str(input())
print(is_correct_bracket_seq(inputStr))