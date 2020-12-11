# 15 сен 2020, 20:27:16 - ID - 34485564


def get_max_path(root, result, left_max=0, right_max=0):
    if root.left:
        left_max, result = get_max_path(root.left, result)

    if root.right:
        right_max, result = get_max_path(root.right, result)

    result = max(root.value, result)
    max_path = root.value

    if root.left:
        result = max(root.value + left_max, result)
        max_path = max(root.value + left_max, max_path)

    if root.right:
        result = max(root.value + right_max, result)
        max_path = max(root.value + right_max, max_path)

    if root.left and root.right:
        result = max(root.value + left_max + right_max, result)

    return max_path, result


def solution(root):
    return get_max_path(root,  root.value)[1]

# Ура, ура, ура) так лучше! Спасибо вам большое, Даша! Можно к вам в команду?)))