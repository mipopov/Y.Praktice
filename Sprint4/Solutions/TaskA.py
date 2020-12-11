# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
#

def solution(node, max_elem= float("-inf")) -> int:
    if node.value > max_elem:
        max_elem = node.value

    if node.left:
        max_elem = solution(node.left, max_elem)

    if node.right:
        max_elem = solution(node.right, max_elem)

    return max_elem

# th_e = Node(8)
# f_e = Node(15)
# first_e = Node(9, f_e, th_e)
# second_e = Node(11)
# tree_root = Node(10, first_e, second_e)
#
# print(solution(tree_root))