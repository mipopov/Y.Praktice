if __name__ == "__main__":
    n = int(input())
    input_str = input()
    count = float("+inf")
    if n == 1:
        print(len(input_str))
    else:
        i = 1
        while i < n:
            new_string = input()
            k = 0
            for j in range(min(len(input_str), len(new_string))):
                if input_str[j] != new_string[j]:
                    k = j
                    break
                else:
                    k += 1

            count = min(count, k)
            i += 1
        print(count)