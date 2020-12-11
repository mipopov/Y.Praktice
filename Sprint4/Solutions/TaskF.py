# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def solution(root):
    max_height = get_max_height(root)
    res_arr = []
    step = 0
    while len(res_arr) < max_height:
        res_arr, dep = get_left_elems(root, res_arr, len(res_arr) - step)
        if root.right:
            root = root.right
            step += 1
        else:
            break
    return res_arr

def get_left_elems(root, res=[], current_height=0, depth= 0):
    if depth >= current_height:
        res.append(root.value)
    depth += 1
    if root.left:
        res, depth = get_left_elems(root.left, res, current_height, depth)
    elif root.right:
        res, depth = get_left_elems(root.right, res, current_height, depth)
    return res, depth

def get_max_height(root):
    if root is None:
        return 0
    left_height = 1 + get_max_height(root.left)
    right_height = 1 + get_max_height(root.right)
    return max(left_height, right_height)
#
#
# root = Node(1, Node(2, Node(4), Node(5)), Node(3,Node(8, Node(17)), Node(10, Node(14))))
# print(solution(root))