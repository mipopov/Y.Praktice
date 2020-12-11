def sort_matrix_by_up_diag(matr, n, m):
    sort_arr = [[] for i in range(m)]

    for i in range(n):
        for j in range(i, m):
            sort_arr[j - i].append(matr[i][j])

    for i in range(m):
        sort_arr[i].sort()

    for i in range(n):
        for j in range(i, m):
            matr[i][j] = sort_arr[j - i][i]


def sort_matr_by_down_diag(matr, n, m):
    sort_arr = [[] for i in range(n - 1)]

    for i in range(1, n):
        for j in range(i):
            if j >= m:
                break
            sort_arr[i - j - 1].append(matr[i][j])

    for i in range(n - 1):
        sort_arr[i].sort()

    for i in range(1, n):
        for j in range(i):
            if j >= m:
                break
            matr[i][j] = sort_arr[i - j - 1][j]


def sort_matr_by_diag(matr, n, m):
    if m != 1 and n != 1:
        sort_matrix_by_up_diag(matr, n, m)
        sort_matr_by_down_diag(matr, n, m)
        return matr
    return matr


def print_matr(matr, n, m):
    for i in range(n):
        for j in range(m):
            print(matr[i][j], end=" ")
        print()


if __name__ == "__main__":
    n = int(input())
    if n > 0:
        m = int(input())
        if m > 0:
            arr = []
            for i in range(n):
                input_arr = [int(j) for j in input().split()]
                arr.append(input_arr)
            print_matr(sort_matr_by_diag(arr, n, m), n, m)