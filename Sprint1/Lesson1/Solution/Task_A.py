inputStr = input().split()

if len(inputStr) == 4:
    print(int(inputStr[0]) * int(inputStr[1]) ** 2 + int(inputStr[2]) * int(inputStr[1]) + int(inputStr[3]))