def get_chunks(arr, n):
    answer = 0
    max_count = 0
    for i in range(n):
        max_count = max(max_count, arr[i])
        if max_count == i:
            answer += 1
    return answer


if __name__ == "__main__":
    n = int(input())
    input_arr = [int(elem) for elem in input().split()]
    print(get_chunks(input_arr, n))