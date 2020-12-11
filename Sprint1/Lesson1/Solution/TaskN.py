n = int(input())

k = 0
while n % 4 == 0:
    k = k + (n // 4)
    n = n // 4

if n <= 4:
    print("True")
else:
    print("False")