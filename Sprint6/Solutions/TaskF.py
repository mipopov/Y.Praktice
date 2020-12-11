# def solution(input_str, find_str, pattern, find_len):
#     new_string = ""
#     i = 0
#     while i < len(input_str):
#         if input_str[i] == find_str[0]:
#             if input_str[i: i + find_len] == find_str:
#                 new_string += pattern
#                 i += find_len
#             else:
#                 new_string += input_str[i]
#                 i += 1
#         else:
#             new_string += input_str[i]
#             i += 1
#     return new_string


def kmp(s):
    p = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        j = p[i - 1]
        while j > 0 and s[j] != s[i]:
            j = p[j - 1]
        if s[j] == s[i]:
            j += 1
        p[i] = j
    return p

if __name__ == "__main__":
    input_str = input()
    find_str = input()
    pattern = input()
    p_arr = kmp(find_str + "#" + input_str)
    print(p_arr)
    # print(input_str.replace(find_str, pattern))
    # print(solution(input_str, find_str, pattern, len(find_str)))