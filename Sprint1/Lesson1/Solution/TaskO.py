firstArray = input().split()
m = int(input())
k = int(input())
firstArray.extend(input().split())
for i in range(len(firstArray)):
    firstArray[i] = int(firstArray[i])
firstArray = sorted(firstArray)
for i in range(k, len(firstArray)):
    print(firstArray[i], end= " ")


