file = open('input.txt')
k = int(file.readline().strip())
n = int(file.readline().strip())
moneyArray = [int(x) for x in file.readline().split()]

def canPartision(arr, k, n):
    if k == 0 or sum(arr) % k != 0:
        return False
    return canPartitionStep(0, arr, [0] * n, k, 0, sum(arr) // k)

def canPartitionStep(itStart, items, used, k, inProgress, targetSum):
    if k == 1:
        return True
    if (inProgress == targetSum):
        return canPartitionStep(0, items, used, k-1, 0, targetSum)

    for i in range(itStart, len(items)):
        if (not used[i]):
            used[i] = True
            if canPartitionStep(i + 1, items, used, k, inProgress + items[i], targetSum):
                return True
            used[i] = False
    return False

print(canPartision(moneyArray, k, n))

