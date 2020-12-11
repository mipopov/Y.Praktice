def get_answer(first_arr, n, second_arr, m, k):
    res_arr = []
    for i in second_arr:
        for j in first_arr:
            res_arr.append((i + j, j, i))

    res_arr.sort(key=lambda x: x[1])

    for i in range(len(res_arr)):
        res_arr[i] = (res_arr[i][0], min(res_arr[i][1], res_arr[i][2]), max(res_arr[i][1], res_arr[i][2]))

    res_arr.sort(key=lambda x: x[0])
    res_arr = res_arr[:k]
    res_arr.sort(key=lambda x: x[1])
    return res_arr


if __name__ == "__main__":
    n1 = int(input())
    if n1 > 0:
        first_arr = [int(x) for x in input().split()]
        n2 = int(input())
        if n2 > 0:
            second_arr = [int(x) for x in input().split()]
            k = int(input())
            if k > 0:
                for pair in get_answer(first_arr, n1, second_arr, n2, k):
                    print(pair[1], pair[2])