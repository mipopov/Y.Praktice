n = int(input())
m = int(input())

inputArray = []
for i in range(n):
    inputArray.append(list(input()))
    
count = 0
for i in range(m):
    for j in range(n-1):
        if (inputArray[j][i] > inputArray[j+1][i]):
             count+=1
             break
print(count)