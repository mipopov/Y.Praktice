strInput = str(input()).lower()

def isPalindrom(myStr):
    strInput = ""
    for i in range(len(myStr)):
        if myStr[i].isalpha():
            strInput += myStr[i]
    if strInput[:: -1] == strInput:
        return True
    else:
        return False

print(isPalindrom(strInput))
