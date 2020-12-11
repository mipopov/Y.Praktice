# def makeDict(arr):
#     newDict = {}
#     for i in arr:
#         if newDict.get(i):
#             old_count = newDict.get(i)
#             newDict.update({i: old_count + 1})
#         else:
#             newDict.update({i: 1})
#     return newDict
#
#
# def isAnagram(str1, str2):
#     return makeDict(str1) == makeDict(str2)
#
#
# firstStr = input().strip()
# secondStr = input().strip()
#
# def countAnagramm(firstStr, secondStr):
#     newLine = firstStr[:len(secondStr)]
#     k = 0
#     if isAnagram(newLine, secondStr):
#         k = 1
#     for i in range(len(secondStr) + 1, len(firstStr), 1):
#         newLine = newLine[1: ] + firstStr[i]
#         if isAnagram(newLine, secondStr):
#             k += 1
#     return k
#
# print(countAnagramm(firstStr,secondStr))

firstStr = input().strip()
secondStr = input().strip()

myDict = dict()
for i in secondStr:
    if i not in myDict:
        myDict[i] = 1
    else:
        myDict[i] += 1

window_count = len(firstStr) - len(secondStr) + 1
window_size = len(secondStr)

resDict = dict()
word_count = 0
for i in range(window_count):
    sub_line = firstStr[i:i + window_size]
    for j in sub_line:
        if j not in myDict:
            break
        else:
            if j not in resDict:
                resDict[j] = 1
            else:
                resDict[j] += 1
    if resDict == myDict:
        word_count += 1
    resDict.clear()



print(word_count)