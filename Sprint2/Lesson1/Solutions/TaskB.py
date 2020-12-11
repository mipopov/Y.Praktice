n = int(input())
inputArray = [int(elem) for elem in input().split()]

moneyCount = 0
i = 1
localMax = inputArray[0]
localMin = localMax

for i in range(1, n):
    if inputArray[i] > localMax:
        localMax = inputArray[i]
    else:
        moneyCount += localMax - localMin
        localMin = inputArray[i]
        localMax = inputArray[i]

moneyCount += localMax - localMin
print(moneyCount)