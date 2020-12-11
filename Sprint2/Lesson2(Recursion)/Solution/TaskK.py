number = 2

def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

def getSqrt(number, roundNum):
    roundNum += 1
    if get_count(number) == 5:
        return number
    return getSqrt(round(number/2 + 1/number, roundNum), roundNum)

print(getSqrt(number, 0))
