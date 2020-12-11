n = int(input())

numbersArray = input().split()

res = 0

k = 0
for i in range(n - 1):
    if int(numbersArray[i]) < int(numbersArray[i + 1]):
        k += 1
    elif int(numbersArray[i]) == int(numbersArray[i + 1]):
        continue
    else:
        if k == 0:
            continue
        elif res < k + 1:
            res = k + 1
            if res >= n - res:
                break
        k = 0

if res < k + 1:
    res = k + 1

print(res)