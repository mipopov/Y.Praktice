def get_cache(arr, n):
    res_sum = 0
    res_sum_dict = {}
    current_len = 0
    for index in range(n):
        if arr[index] == "0":
            res_sum -= 1
        elif arr[index] == "1":
            res_sum += 1
        else:
            return
        if res_sum == 0:
            current_len = index + 1
        else:
            if res_sum in res_sum_dict:
                current_l = index - res_sum_dict.get(res_sum)
                if current_l > current_len:
                    current_len = current_l
            else:
                res_sum_dict.update({res_sum: index})
    print(current_len)


if __name__ == "__main__":
    n = int(input())
    if n > 0:
        input_string = input().split()
        get_cache(input_string, len(input_string))
    elif n == 0:
        print("0")
