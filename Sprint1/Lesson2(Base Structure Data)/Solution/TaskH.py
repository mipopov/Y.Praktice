# class DoubleConnectedNode:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

def solution(node):
    while node.next:
        node = node.next
    newNode = node
    while node:
        node.next = node.prev
        node.prev = node.next
        node = node.prev

    return newNode


# def pr(node):
#     while node:
#         print(node.value)
#         node = node.next
#
# n1 = DoubleConnectedNode("1")
# n2 = DoubleConnectedNode("2",prev=n1)
# n1.next = n2
# n3 = DoubleConnectedNode("3", prev=n2)
# n2.next = n3
# n4 = DoubleConnectedNode("4", prev=n3)
# n3.next = n4
#
# pr(solution(n1))