inputIdArray = input().split()
k = int(input())

# Считаем сколько студентов из вузов - O(n)
def studentCountDict(arr):
    studentDict = {}

    for i in arr:
        if studentDict.get(i):
            old_count = studentDict.get(i)
            studentDict.update({i: old_count + 1})
        else:
            studentDict.update({i: 1})
    return studentDict

result = studentCountDict(inputIdArray)

resultAnswer = []

for i in range(k):
    maxValue = -1
    maxKey = ""
    for (key, value) in result.items():
        if maxValue < value:
            maxValue = value
            maxKey = key
    result.pop(maxKey)
    resultAnswer.append(maxKey)

for i in resultAnswer:
    print(i, end=" ")
