strInput = input()

phoneDict = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

result = [""]

for j in strInput:
    newArray = []
    for i in result:
        for m in phoneDict[int(j)]:
            newArray.append(i + m)
    result = newArray

for i in result:
    print(i, end=" ")
