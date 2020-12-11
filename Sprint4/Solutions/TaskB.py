# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root, is_balance= True):

    if abs(get_height(root.left) - get_height(root.right)) > 1:
        return False
    if root.left:
        is_balance = solution(root.left, is_balance)

    if root.right:
        is_balance = solution(root.right, is_balance)

    return is_balance

def get_height(node):
    if node is None:
        return -1

    left_height = 1 + get_height(node.left)
    right_height = 1 + get_height(node.right)

    return max(left_height, right_height)

# rl = Node(4)
# rr = Node(8)
# r = Node(7)
# l = Node(2)
# root = Node(0, l, r)
#
# print(solution(root))