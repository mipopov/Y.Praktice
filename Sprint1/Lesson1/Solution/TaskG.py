str1 = str(input())
str2 = str(input())

def makeDict(arr):
    newDict = {}
    for i in arr:
        if newDict.get(i):
            old_count = newDict.get(i)
            newDict.update({i: old_count + 1})
        else:
            newDict.update({i: 1})
    return newDict


def isAnagram(str1, str2):
    if len(str1) == len(str2) :
        return makeDict(str1) == makeDict(str2)
    else:
        return False

print(isAnagram(str1, str2))