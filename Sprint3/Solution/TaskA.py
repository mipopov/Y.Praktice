n = int(input())
inputArray = [int(x) for x in input().split()]


def bubbleSort(arr, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

for i in bubbleSort(inputArray, n):
    print(i, end=" ")