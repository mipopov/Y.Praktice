def solution(n, m):
    my_dict = {}
    i = 0
    while i < m:
        inp_str = input().split()
        f_v = int(inp_str[0])
        s_v = int(inp_str[1])
        if s_v != f_v:
            if my_dict.get(f_v):
                my_dict[f_v].add(s_v)
            else:
                my_dict[f_v] = {s_v}

            if my_dict.get(s_v):
                my_dict[s_v].add(f_v)
            else:
                my_dict[s_v] = {f_v}
        i += 1
    if len(my_dict) == 0 and n > 1:
        return "NO"
    new_l = 0
    for (vert, sets) in my_dict.items():
        if new_l == 0:
            new_l = len(sets)
        elif new_l != len(sets):
            return "NO"
    return "YES"


if __name__ == "__main__":
    input_str = input().split()
    n = int(input_str[0])
    m = int(input_str[1])
    print(solution(n, m))


