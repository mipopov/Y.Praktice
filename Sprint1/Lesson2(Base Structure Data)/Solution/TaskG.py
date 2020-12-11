# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
#

def solution(head, inputValue):
    i = 0
    while head:
        if head.value == inputValue:
            return i
        head = head.next_item
        i += 1
    if head:
        return i
    return -1

# n4 = Node("4")
# n3 = Node("3", n4)
# n2 = Node("2", n3)
# n1 = Node("1", n2)
# print(solution(n1, "2"))
