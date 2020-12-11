def get_dict(arr, res_set):
    result_dict = {}
    for elem in arr:
        if elem in res_set:
            if result_dict.get(elem):
                old_value = result_dict.get(elem)
                result_dict.update({elem: old_value + 1})
            else:
                result_dict.update({elem: 1})
    return result_dict

def get_result(first_arr, second_arr):
    result_set = set(second_arr).intersection(set(first_arr))
    count_dict = get_dict(second_arr, result_set)
    for elem in first_arr:
        if elem in result_set and count_dict.get(elem) > 0:
            old_value = count_dict.get(elem)
            count_dict.update({elem: old_value - 1})
            print(elem, end=" ")


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    if m != 0 and n != 0:
        first_array = [int(x) for x in input().split()]
        second_array = [int(x) for x in input().split()]
        get_result(first_array, second_array)