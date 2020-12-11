# 24 авг 2020, 19:43:57 - ID - 33835813
def search_element(arr, left, right, x):
    middle_index = (left + right) // 2
    if x == arr[middle_index]:
        return middle_index

    if right < left:
        return -1

    if arr[left] < arr[middle_index]:
        if arr[left] <= x < arr[middle_index]:
            return search_element(arr, left, middle_index - 1, x)
        else:
            return search_element(arr, middle_index + 1, right, x)
    else:
        if arr[middle_index] < x <= arr[right]:
            return search_element(arr, middle_index + 1, right, x)
        else:
            return search_element(arr, left, middle_index - 1, x)

if __name__ == "__main__":
    file = open('input.txt')
    n = int(file.readline().strip())
    k = int(file.readline().strip())
    input_array = [int(x) for x in file.readline().split()]
    print(search_element(input_array, 0, n - 1, k))


#Спасибо большое за комментарии!!! Особенно в задаче А, где можно обойтись без кортежа, ценно!
# if __name__ == "__main__": - а это нужно, чтобы понимать что в каком порядке вызывается и где? как int main() в С++?