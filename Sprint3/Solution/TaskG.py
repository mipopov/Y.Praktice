def merge_sort(array, n):
    if n < 2:
        return array
    middle_index = n // 2
    left_arr = merge_sort(array[: middle_index], middle_index)
    right_arr = merge_sort(array[middle_index:], n - middle_index)
    return merge_array(left_arr, middle_index, right_arr, n - middle_index)


def merge_array(first, n, second, m):
    result = []
    i, j = 0, 0
    while i < n and j < m:
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    while i < n:
        result.append(first[i])
        i += 1

    while j < m:
        result.append(second[j])
        j += 1

    return result


def count_perim(arr, n):
    for i in range(n - 1, 1, -1):
        first_side = arr[i]
        second_side = arr[i - 1]
        third_side = arr[i - 2]
        if first_side < second_side + third_side \
                and second_side < first_side + third_side \
                and third_side < first_side + second_side:
            return first_side + second_side + third_side


if __name__ == "__main__":
    n = int(input())
    if n > 2:
        input_array = [int(x) for x in input().split()]
        sort_arr = merge_sort(input_array, n)
        print(count_perim(sort_arr, n))

