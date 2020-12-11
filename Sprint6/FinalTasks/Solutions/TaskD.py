# 19 ноя 2020, 23:54:50 - ID - 42041556
def kmp(s, n):
    p = [0 for _ in range(n)]
    for i in range(1, n):
        j = p[i - 1]
        while j > 0 and s[j] != s[i]:
            j = p[j - 1]
        if s[j] == s[i]:
            j += 1
        p[i] = j
    return p


if __name__ == "__main__":
    new_string = input()
    n = len(new_string)
    p = kmp(new_string, n)
    print(n // (n - p[n - 1]))