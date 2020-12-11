f = open('input.txt')
symbol = str(f.read())

eng = 'abcdefghijklmnopqrstuvwxyz'
indexS = eng.index(symbol)


def getLineAlth(ind):
    if ind == 0:
        return "a"
    return getLineAlth(ind - 1) + " " + eng[ind]


print(getLineAlth(indexS))
