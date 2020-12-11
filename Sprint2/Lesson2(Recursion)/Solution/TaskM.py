file = open('input.txt')
l = int(file.readline().strip())
w = int(file.readline().strip())

def getNode(a, b):
    if b == 0:
        return a
    return getNode(b, a % b)

print(getNode(l, w))