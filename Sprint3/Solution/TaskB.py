n = int(input())
inputArray = [int(x) for x in input().split()]


def intersectionSort(arr, n):
    for i in range(n - 1):
        while arr[i + 1] < arr[i] and i >= 0:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
            i -= 1
    return arr

for elem in intersectionSort(inputArray, n):
    print(elem, end=" ")