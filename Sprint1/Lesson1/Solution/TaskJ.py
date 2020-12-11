n = int(input())
inputArr = input().split()

def getDict(arr):
    numberDict = {}

    for i in arr:
        if numberDict.get(int(i)):
            old_count = numberDict.get(int(i))
            numberDict.update({int(i): old_count + 1})
        else:
            numberDict.update({int(i): 1})
    return numberDict

for (key, value) in getDict(inputArr).items():
    if value != 2:
        print(key)
        break
