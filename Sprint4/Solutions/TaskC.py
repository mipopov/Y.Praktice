# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def solution(root, depth= 0, res_arr= []) -> [[]]:
    if len(res_arr) != depth:
        res_arr[depth].append(root.value)
        depth += 1
    else:
        res_arr.append([root.value])
        depth += 1

    if root.left:
        res_arr = solution(root.left, depth, res_arr)

    if root.right:
        res_arr = solution(root.right, depth, res_arr)

    return res_arr
#
#
# r1l1 = Node(21)
# r1 = Node(54, r1l1)
#
# l1l1 = Node(32)
# l1r1 = Node(17)
# l1 = Node(28, l1l1, l1r1)
# root = Node(36, l1, r1)
#
# print(solution(root))

