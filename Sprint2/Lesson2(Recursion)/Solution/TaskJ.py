file = open('input.txt')
n = int(file.readline().strip())
k = int(file.readline().strip())

s = 0
def getIndex(k, s):
    if (k == 1):
        return 0

    if (k == 2):
        return (s + 1) % 2

    if (k % 2 == 0):
        if (s == 0):
            s = 1
        else:
            s = 0
    return getIndex(k // 2 + k % 2, s)
print(getIndex(k, s))

