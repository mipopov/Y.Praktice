# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def solution(root1, root2, is_equal= True) -> bool:
    if root1.value != root2.value:
        return False

    if root2.left and root1.left:
        is_equal = solution(root1.left, root2.left, is_equal)

    elif root2.left and root1.left is None or root2.left is None and root1.left:
        return False

    if root2.right and root1.right:
        is_equal = solution(root1.right, root2.right, is_equal)

    elif root2.right and root1.right is None or root1.right and root2.right is None:
        return False

    return is_equal

#
#
#
# second_e = Node(3)
# left_e = Node(2)
# tree_root = Node(1, left_e, second_e)
#
# second_e_1 = Node(2)
# tree_root_1 = Node(1, left=second_e_1)
# print(solution(tree_root, tree_root))



