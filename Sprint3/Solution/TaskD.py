def get_result(first_arr, second_arr):
    actually_arr = []
    result_set = set(second_arr).intersection(set(first_arr))
    for elem in first_arr:
        if elem not in actually_arr and elem in result_set:
            actually_arr.append(elem)
            print(elem, end=" ")


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    if m != 0 and n != 0:
        first_array = [int(x) for x in input().split()]
        second_array = [int(x) for x in input().split()]
        get_result(first_array, second_array)