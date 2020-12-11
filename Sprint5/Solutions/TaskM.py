def solution(pattern, line):
    if len(pattern) != len(line):
        return "NO"
    h1 = {}
    h2 = {}
    for i in range(len(line)):
        if pattern[i] not in h1 or line[i] not in h2:
            h1[pattern[i]] = line[i]
            h2[line[i]] = pattern[i]
            if len(h1) != len(h2):
                return "NO"
        elif h1[pattern[i]] != line[i] or h2[line[i]] != pattern[i]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    pattern_str = input()
    line_arr = input().split()
    print(solution(pattern_str, line_arr))