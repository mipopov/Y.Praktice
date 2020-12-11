n = int(input())
inputArray = [int(elem) for elem in input().split()]


def getEffectiveSum(a):
    resultSum = sum(a)
    if resultSum % 2 == 1:
        return False

    resultSum //= 2

    combinationArray = [False] * (resultSum + 1)
    combinationArray[0] = True

    for num in a:
        if num > resultSum:
            return False
        for i in range(resultSum, num - 1, -1):
            combinationArray[i] = combinationArray[i] or combinationArray[i - num]
            if combinationArray[-1] == True:
                return True

    return combinationArray[-1]

print(getEffectiveSum(inputArray))