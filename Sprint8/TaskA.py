INF = 100000000
MY_CONST = 500


def get_dp_arr(n, value1, value2):
    dp = [[0] * (n + 1)] * (n + 1)
    for i in range(0, n + 1):
        for j in range(i + 1, n + 1):
            dp[i][j] = INF

    dp[1][0] = value1
    dp[1][1] = value2

    for i in range(2, n + 1):
        dp[i][0] = INF

    return dp


if __name__ == "__main__":
    n = int(input())
    costs = [0] * (n + 1)
    for i in range(1, n + 1):
        costs[i] = int(input())

    dp = []
    if costs[1] > MY_CONST:
        dp = get_dp_arr(n, costs[1], costs[1])
    else:
        dp = get_dp_arr(n, costs[1], INF)

    for i in range(2, n + 1):
        for j in range(0, n + 1):
            if costs[i] <= MY_CONST:
                dp[i][j] = min(dp[i - 1][j] + costs[i], dp[i - 1][j + 1])
            else:
                if j > 0:
                    dp[i][j] = min(int(dp[i - 1][j - 1]) + costs[i], dp[i - 1][j + 1])
                else:
                    dp[i][j] = dp[i - 1][j + 1]

            if dp[i][j] > INF:
                dp[i][j] = INF

    row = 0
    while row < n and dp[n][row] >= dp[n][row + 1] > 0:
        row += 1

    Total_res = dp[n][row]

    days = []
    line = n
    while line > 0:
        if dp[line][row] == dp[line - 1][row + 1]:
            days.append(line)
            line -= 1
            row += 1
            continue
        line -= 1
        if costs[line + 1] > n:
            row -= 1

    print(Total_res, len(days))
    print(*days)
