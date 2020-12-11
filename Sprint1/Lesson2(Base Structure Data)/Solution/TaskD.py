n = int(input())
m = int(input())

a = []

for i in range(n):
    row = input().split()
    a.append(row)

strokePos = int(input())
rowPos = int(input())

if n == 1:
    if m == 1:
        print("")
    else:
        if rowPos == 0:
            print(a[strokePos][rowPos + 1])
        elif rowPos == m - 1:
            print(a[strokePos][rowPos - 1])
        else:
            lI = int(a[strokePos][rowPos - 1])
            rI = int(a[strokePos][rowPos + 1])
            print(min(rI, lI), max(rI, lI))
elif m == 1:
    if n == 1:
        print(" ")
    else:
        if strokePos == 0:
            print(a[strokePos + 1][rowPos])
        elif strokePos == n - 1:
            print(a[strokePos - 1][rowPos])
        else:
            uI = int(a[strokePos - 1][rowPos])
            dI = int(a[strokePos + 1][rowPos])
            print(min(dI, uI), max(dI, uI))
elif strokePos > 0 and strokePos < n - 1 and rowPos > 0 and rowPos < m - 1:
    uI = int(a[strokePos - 1][rowPos])
    dI = int(a[strokePos + 1][rowPos])
    lI = int(a[strokePos][rowPos - 1])
    rI = int(a[strokePos][rowPos + 1])
    for i in sorted([uI, dI, lI,rI]):
        print(i, end= " ")
elif strokePos == 0:
    if rowPos == 0:
        dI = int(a[strokePos + 1][rowPos])
        rI = int(a[strokePos][rowPos + 1])
        print(min(rI, dI), max(rI, dI))
    elif rowPos == m - 1:
        dI = int(a[strokePos + 1][rowPos])
        lI = int(a[strokePos][rowPos - 1])
        print(min(lI, dI), max(lI, dI))
    else:
        dI = int(a[strokePos + 1][rowPos])
        lI = int(a[strokePos][rowPos - 1])
        rI = int(a[strokePos][rowPos + 1])
        for i in sorted([lI, dI, rI]):
            print(i, end= " ")
elif strokePos == n - 1:
    if rowPos == 0:
        uI = int(a[strokePos - 1][rowPos])
        rI = int(a[strokePos][rowPos + 1])
        print(min(rI, uI),max(rI, uI))
    elif rowPos == m - 1:
        uI = int(a[strokePos - 1][rowPos])
        lI = int(a[strokePos][rowPos - 1])
        print(min(lI, uI), max(lI, uI))
    else:
        uI = int(a[strokePos - 1][rowPos])
        lI = int(a[strokePos][rowPos - 1])
        rI = int(a[strokePos][rowPos + 1])
        for i in sorted([lI, uI, rI]):
            print(i, end= " ")
else:
    if rowPos == 0:
        uI = int(a[strokePos - 1][rowPos])
        dI = int(a[strokePos + 1][rowPos])
        rI = int(a[strokePos][rowPos + 1])
        for i in sorted([uI, rI, dI]):
            print(i, end= " ")
    elif rowPos == m - 1:
        uI = int(a[strokePos - 1][rowPos])
        dI = int(a[strokePos + 1][rowPos])
        lI = int(a[strokePos][rowPos - 1])
        for i in sorted([uI,lI,dI]):
            print(i, end= " ")
