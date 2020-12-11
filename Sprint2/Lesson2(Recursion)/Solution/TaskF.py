f = open('input.txt')
n = int(f.read().strip())

res = 1
for i in range(1, n + 1):
    res *= i

print(res)