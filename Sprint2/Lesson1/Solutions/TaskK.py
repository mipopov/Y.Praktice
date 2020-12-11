inputString = input().split()
n = int(inputString[0])
budget = int(inputString[1])

costArray = [int(elem) for elem in input().split()]

if min(costArray) > budget:
    print("0")
elif min(costArray) == budget:
    print("1")
else:
    k = 0
    for i in sorted(costArray):
        if i <= budget:
            k += 1
            budget -= i
    print(k)