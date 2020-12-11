def check(number):
    i = 1
    odd_sum = 0
    even_sum = 0

    while number > 0:
        if i % 2 != 0:
            odd_sum += number % 10
        else:
            even_sum += number % 10
        i += 1
        number //= 10
    return odd_sum == even_sum


if __name__ == "__main__":
    n = int(input())
    first_num = int("1" + "0"*(n - 1))
    second_num = int("10" + "0" * (n - 1))
    if n < 1:
        print("")
    elif n == 1:
        print(0)
    else:
        for i in range(first_num, second_num):
            if check(i):
                print(i)
