def get_unique_dict(string):
    new_set = set()
    result_str = ""
    for i in range(len(string) - 1, -1, -1):
        if string[i] in new_set:
            continue
        else:
            result_str += string[i]
            new_set.add(string[i])

    return result_str


if __name__ == "__main__":
    n = int(input())
    input_str = input()
    if n < 1:
        print("")
    elif n == 1:
        print(input_str)
    else:
        i = 1
        count = float("+inf")
        input_str = get_unique_dict(input_str)
        res_str = ""
        while i < n:
            new_string = get_unique_dict(input())
            k_string = ""
            for j in range(min(len(input_str), len(new_string))):
                if input_str[j] == new_string[j]:
                    k_string += input_str[j]
                else:
                    break
            if len(k_string) < len(res_str) or res_str == "":
                res_str = k_string
            i += 1

        print(res_str[:: -1])
