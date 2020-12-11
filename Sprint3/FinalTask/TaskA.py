# 7 сен 2020, 10:05:23 - ID - 34116459
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
        if first[i] + second[j] > second[j] + first[i]:
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


if __name__ == "__main__":
    n = int(input())
    if n > 0:
        result_string = ""
        for elem in merge_sort(input().split(), n):
            result_string += elem
        print(result_string)

# я что-то заморочился с задачей и сначала сделал только лексикографическую сортировку, она не прокатила, и я что-то напридумывал;
# Сейчас действительно лучше, Дарья, вы так имели ввиду сделать (line 17)