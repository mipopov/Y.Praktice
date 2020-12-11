n = int(input())

lessonArray = []

i = 0
while i < n:
    inputString = input().split()
    lessonArray.append((float(inputString[0]), float(inputString[1])))
    i += 1

lessonArray = sorted(lessonArray, key=lambda x: x[::-1])

earlyLessonBegin = lessonArray[0][0]
earlyLessonEnd = lessonArray[0][1]

result = [(earlyLessonBegin, earlyLessonEnd)]

for i in range(1, len(lessonArray)):
    if lessonArray[i][0] < earlyLessonEnd:
        continue
    elif lessonArray[i][1] == earlyLessonEnd:
        if lessonArray[i][1] == lessonArray[i][0]:
            result.append((lessonArray[i][0], lessonArray[i][1]))
            earlyLessonEnd = lessonArray[i][1]
        else:
            continue
    else:
        result.append((lessonArray[i][0], lessonArray[i][1]))
        earlyLessonEnd = lessonArray[i][1]

print(len(result))

for i in result:
    print(('%f' % i[0]).rstrip('0').rstrip('.'), ('%f' % i[1]).rstrip('0').rstrip('.'))