n = int(input())
scoreArray = input().split()
for i in range(n):
    scoreArray[i] = int(scoreArray[i])
j = 0
i = 0
while i < n:
    if scoreArray[i] == 0:
        if j != 0:
            while j < n:
                if scoreArray[j] != 0:
                    scoreArray[i], scoreArray[j] = scoreArray[j], scoreArray[i]
                    break
                else:
                    j += 1
        else:
            j = i + 1
            while j < n:
                if scoreArray[j] != 0:
                    scoreArray[i], scoreArray[j] = scoreArray[j], scoreArray[i]
                    break
                else:
                    j += 1
        i += 1
    else:
        i += 1

for i in scoreArray:
    if i != 0:
        print(i, end=" ")
    else:
        break
