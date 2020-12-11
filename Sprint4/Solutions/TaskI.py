# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
#

def solution(root):
    return is_BST(root)


def is_BST(node, min_value=float("-inf"), max_value=float("+inf")):
    if node is None:
        return True

    if node.value <= min_value or max_value <= node.value:
        return False

    return is_BST(node.left, min_value, node.value) and is_BST(node.right, node.value, max_value)

# root = Node(5, Node(3, Node(1), Node(5)), Node(8))
# print(solution(root))