# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
#
# def pr(node):
#      while node:
#         print(node.value)
#         node = node.next_item

def solution(head, deleteNumber):
    if deleteNumber == 0:
        return head.next_item
    previousNode = head
    currentNode = head
    i = 0
    while i != deleteNumber:
        previousNode = currentNode
        currentNode = currentNode.next_item
        i += 1
    previousNode.next_item = currentNode.next_item
    return head
#
# n4 = Node("4")
# n3 = Node("3", n4)
# n2 = Node("2", n3)
# n1 = Node("1", n2)
#
# pr(solution(n1, 3))