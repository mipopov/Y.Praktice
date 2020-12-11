n = int(input())
strArray = input().split()

def getDict(arr):
    numberDict = {}

    for i in arr:
        if numberDict.get(i):
            old_count = numberDict.get(i)
            numberDict.update({i: old_count + 1})
        else:
            numberDict.update({i: 1})
    return numberDict

for (key, value) in getDict(strArray).items():
    if value > 1:
        print(key)
        break