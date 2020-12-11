if __name__ == "__main__":
    n = int(input())
    i = 0
    arr = set(".")
    while i < n:
        help_set = set("")
        m = int(input())
        input_str = input().split()

        for elem in arr:
            for j in input_str:
                help_set.add(elem + j + " ")
        arr = help_set
        i += 1
    arr = sorted(arr)
    for elem in arr:
        print(elem.replace(".", ""))