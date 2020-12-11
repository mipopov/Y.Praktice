inputStr = str(input())

def getMaxLenSubStr(myStr):
    maxLen = 0
    while len(myStr) > 0:
        inputStr = " "
        k = 0
        for j in range(len(myStr)):
            if myStr[j] not in inputStr:
                k += 1
                inputStr += myStr[j]
            else:
                break
        if k > maxLen:
            maxLen = k
        myStr = myStr[1:]
    return maxLen

print(getMaxLenSubStr(inputStr))