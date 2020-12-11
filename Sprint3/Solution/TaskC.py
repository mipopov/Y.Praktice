def quick_sort(items, left, right):
    if left < right:
        idx = partision(items, left, right)
        quick_sort(items, left, idx)
        quick_sort(items, idx + 1, right)

def partision(items, left, right):
    pivot_value = items[right - 1]
    i = left

    for j in range(left, right - 1):
        if items[j] <= pivot_value:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[right - 1] = items[right - 1], items[i]
    return i



if __name__ == "__main__":
    n = int(input())
    inputArray = [int(x) for x in input().split()]
    quick_sort(inputArray, 0, n)
    for elem in inputArray:
        print(elem, end=" ")