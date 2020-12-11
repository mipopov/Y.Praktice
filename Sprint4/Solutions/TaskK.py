# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
#

def solution(root):
    result = 0
    for elem in find_path(root):
        result += int(elem)

    return result

def find_path(node, current_paths="", result_ans=[]):
    if node is None:
        return

    current_paths += str(node.value)
    if node.left is None and node.right is None:
        result_ans.append(current_paths)

    if node.left:
        find_path(node.left, current_paths, result_ans)

    if node.right:
        find_path(node.right, current_paths, result_ans)

    return result_ans
#
# root = Node(1, Node(3), Node(5))
# print(solution(root))