def solution(n, arr):
    sum_arr = sum(arr) // 2
    if sum_arr < n:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    n = int(input())
    input_str = [int(x) for x in input().split()]
    print(solution(n, input_str))