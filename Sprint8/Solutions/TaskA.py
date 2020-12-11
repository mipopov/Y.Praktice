MOD = pow(10, 9) + 7

def fibo(n):
    if n <= 2:
        return 1
    arr = [0]* (n + 1)
    arr[1] = 1
    arr[2] = 1

    for i in range(3, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2]) % MOD
    return arr[n]


if __name__ == "__main__":
    n = int(input())
    print(fibo(n + 1))