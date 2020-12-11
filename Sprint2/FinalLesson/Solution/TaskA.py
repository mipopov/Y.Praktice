# 25 авг 2020, 15:19:53 - ID - 33840882
def get_min_and_max_indices(arr, n):
    max_elem = arr[0]
    min_elem = arr[0]
    min_index = 0
    max_index = 0
    for i in range(1, n):
        if arr[i] <= min_elem:
            min_elem = arr[i]
            min_index = i
        elif arr[i] > max_elem:
            max_elem = arr[i]
            max_index = i
    return min_index, max_index


def get_answer(arr, n, max_count):
    while n > 2:
        min_index, max_index = get_min_and_max_indices(arr, n)
        arr[min_index] -= 1
        arr[max_index] -= 1

        if arr[min_index] == 0 and arr[max_index] != 0:
            arr.pop(min_index)
            n -= 1
        elif arr[min_index] != 0 and arr[max_index] == 0:
            arr.pop(max_index)
            n -= 1
        elif arr[min_index] == 0 and arr[max_index] == 0:
            arr.pop(min_index)
            arr.pop(max_index)
            n -= 2
        max_count += 1

    if n <= 1:
        return max_count
    if n == 2:
        return max_count + min(arr)

if __name__ == "__main__":
    file = open('input.txt')
    n = int(file.readline().strip())
    input_array = [int(x) for x in file.readline().split()]
    while 0 in input_array:
        input_array.remove(0)
        n -= 1
    print(get_answer(input_array, n, 0))
