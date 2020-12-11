f = open('input.txt')
a = int(f.readline().strip())
b = int(f.readline().strip())

def linearRepresentation(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = linearRepresentation(b, a % b)
        return d, y, x - y * (a // b)

result = linearRepresentation(a, b)
if a != b:
    print(result[1], result[2], result[0])
else:
    print(min(result[1], result[2]), max(result[1], result[2]), result[0])
