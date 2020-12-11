# 9 сен 2020, 20:38:02 - ID - 34249834
def get_answer(n, our_dict):
    if n in our_dict:
        return our_dict[n]
    res_sum = 0
    for i in range(1, n + 1):
        our_dict[i - 1] = get_answer(i - 1, our_dict)
        res_sum += our_dict[i - 1] * get_answer(n - i, our_dict)
    return res_sum


if __name__ == "__main__":
    n = int(input())
    our_dict = {0: 1, 1: 1}
    print(get_answer(n, our_dict))