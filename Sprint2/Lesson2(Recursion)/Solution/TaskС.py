f = open('input.txt')
n = int(f.read().strip())

def fibo(n):
    if n == 0: return 1
    prev = 0
    current = 1
    next = 0

    for i in range(1, n + 1):
        next = prev + current
        prev = current
        current = next
    return next

print(fibo(n))