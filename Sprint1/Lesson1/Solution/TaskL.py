str1 = str(input())
str2 = str(input())


def getDict(arr):
    numberDict = {}

    for i in arr:
        if numberDict.get(i):
            old_count = numberDict.get(i)
            numberDict.update({i: old_count + 1})
        else:
            numberDict.update({i: 1})
    return numberDict

strDict1 = getDict(str1)
strDict2 = getDict(str2)
if len(strDict2) == len(strDict1):
    for (key, value) in strDict1.items():
        if strDict2.get(key) - value != 0:
            print(key)
else:
    for i in set(strDict1).symmetric_difference(set(strDict2)):
        print(i)
