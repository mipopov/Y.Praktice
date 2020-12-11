def get_dict(arr):
    number_dict = {}
    for i in arr:
        if number_dict.get(i):
            old_count = number_dict.get(i)
            number_dict.update({i: old_count + 1})
        else:
            number_dict.update({i: 1})
    return number_dict


def get_answer(my_dict, model_arr):
    result_string = ""
    for elem in model_arr:
        result_string += (elem + " ") * my_dict.get(elem)
        my_dict.pop(elem)

    lost_string = ""
    for (key, value) in my_dict.items():
        lost_string += (key + " ") * value

    lost_arr = []
    for j in lost_string.split():
        lost_arr.append(int(j))

    lost_arr.sort()

    for j in lost_arr:
        result_string += str(j) + " "

    return result_string


if __name__ == "__main__":
    n = int(input())
    if n > 0:
        need_sort = input().split()
        m = int(input())
        if m > 0:
            model_arr = input().split()
            need_sort_dict = get_dict(need_sort)
            print(get_answer(need_sort_dict, model_arr).strip())
        elif m == 0:
            for elem in sorted(need_sort):
                print(elem, end=" ")
