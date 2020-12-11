def merge_sort(array, n):
    if n < 2:
        return array[:]
    middle_index = n // 2
    left_arr = merge_sort(array[: middle_index], len(array[: middle_index]))
    right_arr = merge_sort(array[middle_index:], len(array[middle_index:]))
    return merge_array(left_arr, right_arr)

def merge_array(first, second):
    result = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    while i < len(first):
        result.append(first[i])
        i += 1

    while j < len(second):
        result.append(second[j])
        j += 1

    return result

if __name__ == "__main__":
    n = int(input())
    if n > 0:
        input_array = [int(x) for x in input().split()]
        for color in merge_sort(input_array, n):
            print(color, end=" ")