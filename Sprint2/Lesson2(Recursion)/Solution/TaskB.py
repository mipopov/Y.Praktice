f = open('input.txt')
n = int(f.read().strip()) + 1

ourDict = {0 : 0, 1 : 1}
def fibo(n):
    if n in ourDict:
        return ourDict[n]
    ourDict[n] = fibo(n-1) + fibo(n-2)
    return ourDict[n]

print(fibo(n))