strInput = str(input())

def getDict(arr):
    numberDict = {}

    for i in arr:
        if numberDict.get(i):
            old_count = numberDict.get(i)
            numberDict.update({i: old_count + 1})
        else:
            numberDict.update({i: 1})
    return numberDict

firstString = ""
secondString = ""
for (key, value) in getDict(strInput).items():
    if value > 1:
        firstString += key * value
    else:
        secondString += key

resultArray = sorted(firstString) + sorted(secondString)
result = ""
for i in resultArray:
    result += str(i)

print(result)