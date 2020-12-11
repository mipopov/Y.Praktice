if __name__ == "__main__":
    pattern = list(input())
    line = input().split()
    if len(line) != len(pattern):
        print("NO")
    h1 = {}
    h2 = {}
    for i in range(len(line)):
        if pattern[i] not in h1 or line[i] not in h2:
            h1[pattern[i]] = line[i]
            h2[line[i]] = pattern[i]
            if len(h1) != len(h2):
                print("NO")
                break
        elif h1[pattern[i]] != line[i] or h2[line[i]] != pattern[i]:
            print("NO")
    return "YES"


