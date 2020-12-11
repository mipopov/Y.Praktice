# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def solution(root):
    return is_symmetric(root, root)


def is_symmetric(node_1, node_2):
    if node_1 is None and node_2 is None:
        return True

    if node_2 and node_1 and node_1.value == node_2.value:
        return is_symmetric(node_1.left, node_2.right) and is_symmetric(node_1.right, node_2.left)

    return False
#
# ll = Node(4)
# lr = Node(3)
# l = Node(2, ll, lr)
#
# rl = Node(4)
# rr = Node(3)
# r = Node(2, rl, rr)
# root = Node(1, l, r)
#
# print(solution(root))