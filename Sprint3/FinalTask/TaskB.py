#3 сен 2020, 21:39:14 - ID - 34025037
def find_median_in(arr_f, n, arr_s, m):
    low = 0
    high = n

    while low <= high:
        partition_first = (low + high) // 2
        partition_second = (n + m + 1) // 2 - partition_first

        max_left_elem_f = arr_f[partition_first - 1] if partition_first > 0 else float('-inf')
        min_right_elem_f = float('inf') if partition_first == n else arr_f[partition_first]

        max_left_elem_s = arr_s[partition_second - 1] if partition_second > 0 else float('-inf')
        min_right_elem_s = float('inf') if partition_second == m else arr_s[partition_second]

        if max_left_elem_f <= min_right_elem_s and min_right_elem_f >= max_left_elem_s:
            if (n + m) % 2 == 0:
                return (max(max_left_elem_f, max_left_elem_s) + min(min_right_elem_f, min_right_elem_s)) / 2
            else:
                return max(max_left_elem_f, max_left_elem_s)

        elif max_left_elem_f > min_right_elem_s:
            high = partition_first - 1
        else:
            low = partition_first + 1


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    first_arr = [int(x) for x in input().split()]
    second_arr = [int(x) for x in input().split()]
    if n > m:
        print(find_median_in(second_arr, m, first_arr, n))
    else:
        print(find_median_in(first_arr, n, second_arr, m))

#Здесь я неочень понял замечание, у нас в примечании написано, что мержить их низя
# "Решение должно работать за O(log(m + n)). Соединять массивы нельзя"
# Если можно было бы мержить, я с радостью бы это сделал))) как в сортровки слиянием(в TaskA)
# Ну и сложность у меня чуть поменьше, O(log(min(m,n)))
# Я по сути ищу 4 числа, которые удовлетворяют определенным условиям, два сверху, два снизу;

