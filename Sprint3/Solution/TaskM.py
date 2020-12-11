def isSubstr(needle, haystack):
    current_pos = 0
    for c in needle:
        current_pos = haystack.find(c, current_pos) + 1
        if current_pos == 0:
            return False
    return True


def get_answer(cipher_string, n):
    res_str = ""
    while n > 0:
        input_string = input().strip()
        if isSubstr(input_string, cipher_string):
            if len(res_str) < len(input_string):
                res_str = input_string
            elif len(res_str) == len(input_string):
                if res_str >= input_string:
                    res_str = input_string
        n -= 1
    return res_str


if __name__ == "__main__":
    cipher_string = input().strip()
    n = int(input())
    print(get_answer(cipher_string, n))
