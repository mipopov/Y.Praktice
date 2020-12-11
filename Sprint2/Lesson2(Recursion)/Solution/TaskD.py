f = open('input.txt')
n = int(f.read().strip()) + 1

def fib_last_digit(n):
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, (a+b) % 10
        return b

print(fib_last_digit(n))