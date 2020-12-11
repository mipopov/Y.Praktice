c = int(input())
n = int(input())

thingsArray =[]

i = 0
while i < n:
    inputStr = input().split()
    thingsArray.append((int(inputStr[0]), int(inputStr[1]), int(inputStr[0])/int(inputStr[1]), i))
    i += 1
thingsArray.sort(key=lambda x: x[1])
thingsArray.sort(key=lambda x: x[0], reverse=True)
# thingsArray.sort(key=lambda x: x[2])

summaryCost = 0
summaryWight = 0
newArr =[]
for i in range(len(thingsArray)):
    if summaryWight + thingsArray[i][1] <= c:
        summaryWight += thingsArray[i][1]
        summaryCost += thingsArray[i][0]
        newArr.append(thingsArray[i][3])

for i in sorted(newArr):
    print(i, end=" ")

