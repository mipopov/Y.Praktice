n = int(input())
m = int(input())

x1 = 0
y1 = 0
x2 = m - 1
y2 = n - 1

counter = 0

array = []
for i in range(n):
    array.append(list(input().split()))


flag = True
step = 1

elCount = m * n
while(flag):
    if step == 1:
        row = array[y1]
        x = x1
        while(x <= x2):
            print(row[x])
            counter += 1
            x+=1
        y1+=1
    elif step == 2:
        y = y1
        while(y <= y2):
            row = array[y]
            print(row[x2])
            counter+=1
            y+=1
        x2-=1
    elif step == 3:
        row = array[y2]
        x = x2
        while(x>=x1):
            print(row[x])
            counter+=1
            x-=1
        y2-=1
    elif step == 4:
        y = y2
        while (y >= y1):
            row = array[y]
            print(row[x1])
            counter+=1
            y-=1
        x1+=1
    if (counter == elCount):
        flag = False
        continue;
    step += 1
    if (step == 5):
        step = 1
