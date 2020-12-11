xCount = int(input())
xNumbersArray = input().split()
k = int(input())

def makeIntNumber(strLen, arr):
    if len(arr) == strLen:
        newString = ""
        for i in arr:
            newString += i
        return int(newString)

def makeNumberArray(number):
    numberArray = []
    while number > 0:
        numberArray.append(number % 10)
        number = number // 10
    return numberArray

result = makeNumberArray(makeIntNumber(xCount,xNumbersArray) + k)
result.reverse()
for i in result:
    print(i, end=" ")
