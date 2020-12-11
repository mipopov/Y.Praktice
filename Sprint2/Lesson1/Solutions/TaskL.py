n = int(input())
stepArray = list(map(int, input().split(" ")))

def getAnswer(arr, n):
    if arr[0] == 0:
        return False
    i = 0
    while i < n:
        if i + arr[i] >= n:
            return True
        newArr = arr[i + 1 : arr[i] + i + 1]
        maxElementInNewArr = max(newArr)
        if maxElementInNewArr == 0:
            return False
        newInd = newArr.index(maxElementInNewArr)
        i += newInd + 1

print(getAnswer(stepArray, n))



# 5
#
# 2 0 10 2
# 9
# 4 1 4 0 0 0 0 0 0
