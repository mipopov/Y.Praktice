if __name__ == "__main__":
    n = int(input())
    keys = input().split()
    m = int(input())
    values = input().split()

    i = 0
    while i < n:
        if i < m:
            print("{}: {}".format(keys[i], values[i]))
        else:
            print("{}: {}".format(keys[i], "None"))

        i += 1

