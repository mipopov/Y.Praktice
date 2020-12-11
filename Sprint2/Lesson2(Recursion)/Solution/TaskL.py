file = open("input.txt")
summa = int(file.readline().strip())
k = int(file.readline().strip())
moneyArray = [int(x) for x in file.readline().split()]
count = 0
index = 0
def getAnswer(arr, idx, last, summa):
    if (summa == 0):
        return 1
    if (summa < 0):
        return 0
    res = 0
    for i in range(idx, len(arr)):
        if (arr[i] >= last and summa - arr[i] >= 0):
            res += getAnswer(arr, i, arr[i], summa - arr[i])
    return res

print(getAnswer(moneyArray, index, moneyArray[0], summa))