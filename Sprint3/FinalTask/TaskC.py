#3 сен 2020, 09:19:45 - ID - 33998876
def radix_sort(arr, max_radix_length):
    digit_count = 10

    for i in range(max_radix_length):
        help_arr = [[] for k in range(digit_count)]

        for elem in arr:
            need_digit = (elem // (10 ** i)) % digit_count
            help_arr[need_digit].append(elem)

        arr = []
        for i in range(digit_count):
            arr += help_arr[i]
    return arr


if __name__ == "__main__":
    n = int(input())
    max_radix_length = 0
    input_arr = []
    for elem in input().split():
        if len(elem) > max_radix_length:
            max_radix_length = len(elem)
        input_arr.append(int(elem))
    print(*radix_sort(input_arr, max_radix_length))

#Oh my God; божественно)) На самом деле я немного путаюсь; я знаю в С++ есть указатели; и там понятно как это работает;
# а питон вроде как указателей нет, то теперь оказалось, что они есть)) погуглю, спасибо!