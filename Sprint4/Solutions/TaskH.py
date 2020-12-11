


def get_answer(n, arr, k):
    result_heap = FibonacciHeap()
    for i in range(n - 1):
        for j in range(i + 1, n):
            result_heap.insert(abs(arr[i] - arr[j]))
    return result_heap.find_min().key


if __name__ == "__main__":
    n = int(input())
    input_arr = [int(x) for x in input().split()]
    k = int(input())
    print(get_answer(n, input_arr, k))