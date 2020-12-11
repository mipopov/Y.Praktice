def get_result(even_arr, odd_arr, n):
    result_arr = []
    i = 0
    while i < n // 2:
        result_arr.append(odd_arr[i])
        result_arr.append(even_arr[i])
        i += 1
    return result_arr

def partision(arr):
    even_arr = []
    odd_arr = []
    for i in arr:
        if i % 2 == 0:
            odd_arr.append(i)
        else:
            even_arr.append(i)
    return even_arr, odd_arr


if __name__ == "__main__":
    n = int(input())
    if n != 0:
        inputArray = [int(x) for x in input().split()]
        even_arr, odd_arr = partision(inputArray)
        for elem in get_result(even_arr, odd_arr, n):
            print(elem, end=" ")

