# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def solution(root):
    return get_max_height(root)

def get_max_height(node):
    if node is None:
        return 0

    left_size = 1 + get_max_height(node.left)
    right_size = 1 + get_max_height(node.right)

    return max(left_size, right_size)

# root = Node(3,Node(1, Node(8), Node(12, Node(5))), Node(4))
# print(solution(root))