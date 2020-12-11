def get_all_numbers(num):
    result = 0
    while num > 0:
        result += (num % 10) ** 2
        num //= 10
    return result

def get_answer(n):
    arr = [0] * 100001
    while arr[n] == 0:
        if n == 1:
            return True
        arr[n] = n
        n = get_all_numbers(n)
    return False


if __name__ == "__main__":
    n = int(input())
    print(get_answer(n))