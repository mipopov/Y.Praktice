childrenCount = int(input())
childrenAppet = input().split()

cryspyCount = int(input())
cryspyCountHealth = input().split()

for i in range(len(childrenAppet)):
    childrenAppet[i] = int(childrenAppet[i])

for i in range(len(cryspyCountHealth)):
    cryspyCountHealth[i] = int(cryspyCountHealth[i])


cryspyCountHealth.sort()
childrenAppet.sort()

count = 0
for i in cryspyCountHealth:
    if count < len(childrenAppet):
        if i >= childrenAppet[count]:
            count += 1
    else:
        break

print(count)
