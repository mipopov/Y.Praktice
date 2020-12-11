MOD = pow(10, 9) + 7


def get_res(n, k):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        j = 1
        while j <= k and i >= j:
            dp[i] += dp[i - j]
            dp[i] %= MOD
            j += 1
    return dp[n]


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(get_res(n, k))

