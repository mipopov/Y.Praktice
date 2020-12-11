n = int(input())
scoreArray = input().split()

for i in range(n):
    scoreArray[i] = int(scoreArray[i])

scoreArray = sorted(scoreArray)

maxResult = -1
for i in range(n - 1):
    left = i + 1
    right = n - 1
    while left < right:
        trippleSum = scoreArray[i] + scoreArray[left] + scoreArray[right]
        if trippleSum == 0:
            maxCount = scoreArray[i] * scoreArray[left] * scoreArray[right]
            if maxCount > maxResult:
                maxResult = maxCount
            left += 1
            right -= 1
        elif trippleSum > 0:
            right -= 1
        else:
            left += 1

print(maxResult)