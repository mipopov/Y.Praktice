n = int(input())
m = int(input())

a = []

for i in range(n):
    row = input().split()
    a.append(row)


for j in range(m):
    for i in range(n):
        print(a[i][j],end= " ")
    print()
