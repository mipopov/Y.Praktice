def get_number_arr(n):
    res_set = {1}
    while len(res_set) <= 7000:
        help_arr = res_set.union({1})
        for i in res_set:
            help_arr.add(i * 2)

        for i in res_set:
            help_arr.add(i * 3)

        for i in res_set:
            help_arr.add(i * 5)

        res_set = help_arr

    return sorted(list(res_set))[n]


if __name__ == "__main__":
    n = int(input())
    print(get_number_arr(n - 1))
