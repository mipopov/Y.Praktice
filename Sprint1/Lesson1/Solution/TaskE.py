n = int(input())

res = ""

while n > 0:
    res = str(n % 2) + res
    n = n // 2

print(res)