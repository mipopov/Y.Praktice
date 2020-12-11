inp = list(map(int, input().split()))
n = inp[0]+1
k = inp[1]+1
matrix = []
matrix.append([0] * k)
for i in range(n-1):
    matrix.append(list(map(int, ('0 ' + input()+' 0').split())))
matrix.append([0] * k)
res = 0
for i in range(1, n):
    for j in range(1, k):
        if matrix[i][j] == 1:
            if matrix[i][j-1] == 0:
                res += 1
            if matrix[i][j+1] == 0:
                res += 1
            if matrix[i-1][j] == 0:
                res += 1
            if matrix[i+1][j] == 0:
                res += 1
print(res)

