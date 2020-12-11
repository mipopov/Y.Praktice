f = open('input.txt')
n = int(f.read().strip())

def getFact(n):
    if n == 0: return 1
    return n * getFact(n - 1)

print(getFact(n))